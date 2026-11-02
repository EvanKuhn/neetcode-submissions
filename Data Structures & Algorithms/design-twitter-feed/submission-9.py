import heapq
from collections import namedtuple

TweetData = namedtuple("TweetData", ["id", "ts"])

class TwitterUser:
    def __init__(self, id: int) -> None:
        self.id = id
        self.tweets: list[TweetData] = []  # List of (tweetId, timestamp) pairs
        self.following: set[int] = set()

    def postTweet(self, tweetId: int, ts: int) -> None:
        self.tweets.append(TweetData(id=tweetId, ts=ts))

    def __str__(self) -> str:
        return f"<User id={self.id} tweets={self.tweets} following={self.following}"

class UserTweetIter:
    def __init__(self, user: TwitterUser) -> None:
        self.user = user
        self.tweet_index = len(user.tweets) - 1  # Counts down to -1

    def peek(self) -> TweetData:
        """Peak at current TweetData"""
        id, ts = self.user.tweets[self.tweet_index]
        return TweetData(id=id, ts=ts)

    def pop(self) -> TweetData:
        """Get current TweetData, and iterate to next"""
        cur: TweetData = self.peek()
        self.tweet_index -= 1
        return cur

    def is_done(self) -> bool:
        return self.tweet_index < 0

    def __lt__(self, other) -> bool:
        return self.peek().ts < other.peek().ts

class Twitter:
    def __init__(self):
        self._ts = -1  # Use simple counter for timestamps
        self._users: dict[int, TwitterUser] = {}

    def _get_ts(self) -> int:
        self._ts += 1
        return self._ts

    def _get_user(self, userId: int) -> TwitterUser:
        if userId not in self._users:
            self._users[userId] = TwitterUser(userId)
        return self._users[userId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._get_user(userId).postTweet(tweetId, self._get_ts())

    def follow(self, followerId: int, followeeId: int) -> None:
        self._get_user(followerId).following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._get_user(followerId).following.discard(followeeId)

    def getNewsFeed(self, userId: int) -> List[int]:
        results = []
        user = self._get_user(userId)
        # print(f"getNewsFeed(): userId={userId} got user {user}")

        # Get collection of all users, including this user.
        # Order by last tweet time.
        users: list[TwitterUser] = [user] + [self._get_user(i) for i in user.following]
        # print(f"user+following({userId}) = {[u.id for u in users]}")

        # ... need to keep track of next tweet (id and timestamp),
        #     and order the heap of users by that timestamp
        heap = [UserTweetIter(u) for u in users if u.tweets]
        heapq.heapify_max(heap)

        # Ten times, do:
        # - Get next user off of heap (this user has latest tweet)
        # - Get and save their tweet
        # - Iterate the UserTweetIter and place back in heap

        for _ in range(0,10):
            if not heap:
                break
            it = heapq.heappop_max(heap)
            if not it.is_done():
                tweet_data = it.pop()
                results.append(tweet_data.id)
            if not it.is_done():
                heapq.heappush_max(heap, it)

        return results


# ["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1], "getNewsFeed", [2], "unfollow", [1, 2], "getNewsFeed", [1]]


# ["Twitter", "postTweet", [1, 101], "postTweet", [1, 102], "follow", [2, 1], "getNewsFeed", [2], "unfollow", [2, 1], "getNewsFeed", [2]]