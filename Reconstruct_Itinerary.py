class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if not tickets:
            return []

        segments = {}
        for i in xrange(len(tickets)):
            if tickets[i][0] not in segments:
                segments[tickets[i][0]] = [tickets[i][1]]
            else:
                segments[tickets[i][0]].append(tickets[i][1])

        for start in segments:
            segments[start].sort(reverse = True)

        to_visit = ['JFK']
        path = []
        while segments:
            print to_visit, path, segments
            cur = to_visit.pop()
            path.append(cur)
            if cur in segments:
                to_visit += segments[cur]
                segments.pop(cur)
            else:
                path.pop()
                segments[path[-1]] = [cur]
        return path

if __name__ == '__main__':
    Solution().findItinerary([["JFK","ATL"],["ORD","PHL"],["JFK","ORD"],["PHX","LAX"],["LAX","JFK"],["PHL","ATL"],["ATL","PHX"]])