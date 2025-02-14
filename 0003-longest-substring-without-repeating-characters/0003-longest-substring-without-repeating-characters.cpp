class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char, int> mp;
        int n = s.length();
        int start = 0, end = 0, mx = 0;

        while (end < n) {
            while (mp[s[end]] == 1 && start < end) {
                mp[s[start]]--;
                start++;
            }
            mp[s[end]]++;
            mx = max(mx, end - start + 1);
            end++;
        }
        return mx;
    }
};