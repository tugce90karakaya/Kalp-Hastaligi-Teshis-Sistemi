import re
class Inference:
    def __init__(self):
        self.rules = self.read_rules()
        print(self.rules)
   
    def read_rules(self):
        rules = []
        with open('rules.fcl') as f:
            for line in f:
                rule = []
                if 'OR' in line:
                    for normal_rule in self.change_to_normal_rule(line):
                        rules.append(normal_rule)
                    continue
                for i in re.split('[()]', line):
                    if 'IS' in i:
                        rule.append(list(i.replace('IS', '').replace('THEN', '').replace(';', '').split()))
                rules.append(rule)
        return rules

    def change_to_normal_rule(self, rule):
        rules = []
        parts = []
        for i in re.split('[()]', rule):
            if 'IS' in i:
                parts.append(list(i.replace('IS', '').replace('THEN', '').replace(';', '').split()))
        for i in range(len(parts)-1):
            rule = []
            rule.append(parts[i])
            rule.append(parts[len(parts)-1])
            rules.append(rule)
        return rules

    def result_membership(self, fuzzy_value):
        result = {
            'healthy': [0],
            'sick_1': [0],
            'sick_2': [0],
            'sick_3': [0],
            'sick_4': [0]}

        for rule in self.rules:
           
            memberships = []
            
            for i in range(len(rule)-1):
                print(rule[i][0],rule[i][1])
                memberships.append(fuzzy_value[rule[i][0]][rule[i][1]])
            print(len(rule)-1)
            result[rule[len(rule)-1][1]].append(min(memberships))
        
        for subset in result:
            result[subset] = max(result[subset])
        return result
