### 4. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

counties = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

china, russia, usa, *scandic_countries = counties
print(scandic_countries)
# ['Finland', 'Sweden', 'Norway', 'Denmark']