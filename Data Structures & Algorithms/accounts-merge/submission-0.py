class Solution:
    def get_group(self, email):
        while email != self.email_groups[email]:
            email = self.email_groups[email]
        
        return email
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        reps = {}
        
        self.email_groups = {}
        
        for acc in accounts:
            groups = set()
            
            for email in islice(acc, 1, None):
                if email in self.email_groups:
                    groups.add(self.get_group(email))
                    
            if groups == set():
                rep = acc[1]
                
                reps[rep] = acc[0]
                
                for email in islice(acc, 1, None):
                    self.email_groups[email] = rep 
            else:
                rep = groups.pop()
                
                for group in groups:
                    self.email_groups[group] = rep
            
                for email in islice(acc, 1, None):
                    if email not in self.email_groups:
                        self.email_groups[email] = rep
                        
        email_lists = {}
        
        for email in self.email_groups:
            group = self.get_group(email)
            
            if group in email_lists:
                email_lists[group].append(email)
            else:
                email_lists[group] = [email]
                
        return [[reps[k]] + sorted(v) for k, v in email_lists.items()]
                