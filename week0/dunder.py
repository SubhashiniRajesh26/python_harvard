class software:
    names = []
    versions = {}
    def __init__(self, names):
        if names:
            self.names = names.copy()
            for name in names:
                self.versions[name] = 1
        else:
            raise Exception("Enter names")
    
    def __str__(self):
        s ="The current softwares and their versions are listed below: \n"
        for key,value in self.versions.items():
            s+= f"{key} : v{value} \n"
        return s

    def __setitem__(self,name,version):
        if name in self.versions:
            self.versions[name] = version
        else:
            raise Exception("Software Name doesn't exist")
    
    def __getitem__(self,name):
        if name in self.versions:
            return self.versions[name]
        else:
            raise Exception("Software Name doesn't exist")

    def __delitem__(self,name):
        if name in self.versions:
            del self.versions[name]
            self.names.remove(name)
        else:
            raise Exception("Software Name doesn't exist")

    def __len__(self):
        return len(self.names)
    
    def __contains__(self,name):
        if name in self.versions:
            return True
        else:
            return False





p = software(['S1', 'S2', "S3"])
p['S1'] = 2
# p['2'] = 2
print(p['S2'])
del p['S1']
print(p)
if 'S2' in p:
    print("Software Exists")
else:
    print("Software DOESN'T exist")

