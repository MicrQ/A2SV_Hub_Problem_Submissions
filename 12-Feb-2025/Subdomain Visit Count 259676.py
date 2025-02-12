# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_count = {}

        # looping through the domains and their visit count
        for visit_domain in cpdomains:

            # separating the visit and the domain
            visit, domain = visit_domain.split()
            visit = int(visit)

            subdomains = domain.split('.')
            # looping through the domain starting from the the lowest level
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])

                if visit_count.get(subdomain) is not None:
                    visit_count[subdomain] += visit

                else:
                    visit_count[subdomain] = visit

        return [f'{visit} {domain}' for domain, visit in visit_count.items()]
