/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    struct Compare {
        bool operator()(const ListNode* a, const ListNode* b) {
            return a->val > b->val;
        }
    };

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, Compare> pq;

        int K = lists.size();

        for (int i = 0; i < K; i++) {
            ListNode* node = lists[i];

            while (node != NULL) {
                pq.push(node);
                node = node->next;
            }
        }

        ListNode* head = NULL, *prev = NULL;
        if (pq.empty()) return NULL;
        while (!pq.empty()) {
            ListNode* node = pq.top();
            pq.pop();
            if (prev != NULL) prev->next = node;
            else head = node;

            prev = node;
        }

        prev->next = NULL;

        return head;
    }
};