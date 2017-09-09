# class Solution(object):
#     def findItinerary(self, tickets):
#         """
#         :type tickets: List[List[str]]
#         :rtype: List[str]
#         """
#         if not tickets:
#             return []

#         segments = {}
#         for i in xrange(len(tickets)):
#             if tickets[i][0] not in segments:
#                 segments[tickets[i][0]] = [tickets[i][1]]
#             else:
#                 segments[tickets[i][0]].append(tickets[i][1])

#         for start in segments:
#             segments[start].sort(reverse = True)

#         to_visit = ['JFK']
#         path = []
#         visited = []
#         while to_visit:
#             cur = to_visit.pop()
#             path.append(cur)
#             visited.append(cur)
#             print 'path: ' + `path`
#             print 'visited' + `visited`
#             if cur not in segments and len(path) <= len(tickets):
#                 path.pop()
#             elif len(path) == len(tickets) + 1:
#                 break
#             else:
#                 to_visit += [stop for stop in segments[cur] if stop not in visited]
#         return path

import collections
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route, stack = [], ['JFK']
        while stack:
            while targets[stack[-1]]:
                stack += targets[stack[-1]].pop(),
            route += stack.pop(),
        return route[::-1]


if __name__ == '__main__':
    print Solution().findItinerary([['JFK', 'ATL'], ['ATL', 'JFK'], ['JFK', 'SFO'], ['SFO', 'JFK']])

