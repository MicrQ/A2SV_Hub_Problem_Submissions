# Problem: Design Authentication Manager - https://leetcode.com/problems/design-authentication-manager/

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time_to_live = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.time_to_live

    def renew(self, tokenId: str, currentTime: int) -> None:
        
        # renewing the token only if it's not expired
        if self.tokens.get(tokenId) and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.time_to_live

    def countUnexpiredTokens(self, currentTime: int) -> int:
        token_count = 0

        for exp_time in self.tokens.values():
            if exp_time > currentTime:
                token_count += 1

        return token_count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)