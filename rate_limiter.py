import time


class RateLimiter:

    def __init__(self, max_requests, refill_rate):
        self.bucket = max_requests
        self.max_requests = max_requests
        self.refills_per_second = refill_rate
        self.last_refill_timestamp = time.time()

    def is_allowed(self, tokens):
        self.refill()

        if tokens <= self.bucket:
            self.bucket -= tokens
            return True

        return False

    def refill(self):
        now = time.time()
        self.bucket = min(self.max_requests, self.bucket + (now - self.last_refill_timestamp) * self.refills_per_second)
        self.last_refill_timestamp = now

    def __str__(self):
        return f"Bucket: {self.bucket}, Last Refill: {self.last_refill_timestamp}, Refills per second: {self.refills_per_second}"

if __name__ == "__main__":
    rate_limiter = RateLimiter(10, 10)
    time.sleep(0.3)
    print(rate_limiter.is_allowed(6))
    print(rate_limiter)
    time.sleep(0.2)
    print(rate_limiter.is_allowed(5))
    print(rate_limiter)
