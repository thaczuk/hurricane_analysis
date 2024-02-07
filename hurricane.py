# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
def convert_damages(damages):
    updated_damages = []

    for damage in damages:
        if damage == 'Damages not recorded':
            updated_damages.append(damage)
        else:
            # Extract the numeric part of the string and convert to float
            value = float(damage[:-1])  # Remove the last character (B or M)
            multiplier = 1_000_000_000 if damage.endswith('B') else 1_000_000  # Determine multiplier (B or M)
            updated_damages.append(value * multiplier)

    return updated_damages

# Example usage
updated_damages = convert_damages(damages)
print(updated_damages)

# 2 
# Create a Table

# Create and view the hurricanes dictionary
def create_hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricanes_dict = {}

    for i in range(len(names)):
        hurricane_data = {
            'Name': names[i],
            'Month': months[i],
            'Year': years[i],
            'Max Sustained Wind': max_sustained_winds[i],
            'Areas Affected': areas_affected[i],
            'Damage': damages[i],
            'Deaths': deaths[i]
        }

        hurricanes_dict[names[i]] = hurricane_data

    return hurricanes_dict
# Example usage
hurricanes_data = create_hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)

# Print the data for hurricane "Cuba I" as an example
print(hurricanes_data['Cuba I'])

# 3
# Organizing by Year
def group_hurricanes_by_year(hurricanes_data):
    hurricanes_by_year = {}

    for hurricane_data in hurricanes_data.values():
        year = hurricane_data['Year']
        if year not in hurricanes_by_year:
            hurricanes_by_year[year] = []

        hurricanes_by_year[year].append({
            'Name': hurricane_data['Name'],
            'Month': hurricane_data['Month'],
            'Year': hurricane_data['Year'],
            'Max Sustained Wind': hurricane_data['Max Sustained Wind'],
            'Areas Affected': hurricane_data['Areas Affected'],
            'Damage': hurricane_data['Damage'],
            'Deaths': hurricane_data['Deaths']
        })

    return hurricanes_by_year

# Example usage
# create a new dictionary of hurricanes with year and key
hurricanes_by_year = group_hurricanes_by_year(hurricanes_data)

# Print the data for the year 1932 as an example
print(hurricanes_by_year[1932])

# 4
# Counting Damaged Areas

def count_affected_areas(hurricanes_data):
    affected_areas_count = {}

    for hurricane_data in hurricanes_data.values():
        areas_affected = hurricane_data['Areas Affected']

        for area in areas_affected:
            if area not in affected_areas_count:
                affected_areas_count[area] = 1
            else:
                affected_areas_count[area] += 1

    return affected_areas_count

# Example usage
# create dictionary of areas to store the number of hurricanes involved in
areas_count = count_affected_areas(hurricanes_data)

# Print the counts of affected areas
print(areas_count)

# 5 
# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in
def most_affected_area(affected_areas_count):
    if not affected_areas_count:
        return None, 0

    most_affected = max(affected_areas_count, key=affected_areas_count.get)
    count = affected_areas_count[most_affected]

    return most_affected, count

# Example usage
most_affected, count = most_affected_area(areas_count)

# Print the most affected area and its count
print(f"The most affected area is '{most_affected}' with {count} hurricanes.")

# 6
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths
def deadliest_hurricane(hurricanes_data):
    max_deaths_hurricane = None
    max_deaths = 0

    for hurricane_data in hurricanes_data.values():
        deaths = hurricane_data['Deaths']
        if deaths > max_deaths:
            max_deaths_hurricane = hurricane_data['Name']
            max_deaths = deaths

    return max_deaths_hurricane, max_deaths

# Example usage
deadliest, death_count = deadliest_hurricane(hurricanes_data)

# Print the deadliest hurricane and its death count
print(f"The deadliest hurricane is '{deadliest}' with {death_count} deaths.")


# 7
# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key
def rate_hurricanes_by_mortality(hurricanes_data, mortality_scale):
    hurricanes_by_mortality = {rating: [] for rating in mortality_scale}

    for hurricane_data in hurricanes_data.values():
        deaths = hurricane_data['Deaths']

        for rating, upper_bound in mortality_scale.items():
            if deaths <= upper_bound:
                hurricanes_by_mortality[rating].append({
                    'Name': hurricane_data['Name'],
                    'Month': hurricane_data['Month'],
                    'Year': hurricane_data['Year'],
                    'Max Sustained Wind': hurricane_data['Max Sustained Wind'],
                    'Areas Affected': hurricane_data['Areas Affected'],
                    'Damage': hurricane_data['Damage'],
                    'Deaths': deaths
                })
                break

    return hurricanes_by_mortality

# Mortality scale
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}

# Example usage
hurricanes_by_mortality = rate_hurricanes_by_mortality(hurricanes_data, mortality_scale)

# Print the hurricanes for each mortality rating
for rating, hurricanes_list in hurricanes_by_mortality.items():
    print(f"\nMortality Rating {rating}:")
    for hurricane in hurricanes_list:
        print(hurricane)

# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost
def costliest_hurricane(hurricanes_data):
    max_damage_hurricane = None
    max_damage = 0

    for hurricane_data in hurricanes_data.values():
        damage = hurricane_data['Damage']

        if damage != 'Damages not recorded':
            # Convert damage to float value
            damage_value = float(damage[:-1]) if damage.endswith('B') else float(damage[:-1]) * 1_000_000
        else:
            damage_value = 0

        if damage_value > max_damage:
            max_damage_hurricane = hurricane_data['Name']
            max_damage = damage_value

    return max_damage_hurricane, max_damage

# Example usage
costliest, damage_amount = costliest_hurricane(hurricanes_data)

# Print the costliest hurricane and its damage amount
print(f"The costliest hurricane is '{costliest}' with damage amount ${damage_amount:.2f}.")


# 9
# Rating Hurricanes by Damage
# categorize hurricanes in new dictionary with damage severity as key
def rate_hurricanes_by_damage(hurricanes_data, damage_scale):
    hurricanes_by_damage = {rating: [] for rating in damage_scale}

    for hurricane_data in hurricanes_data.values():
        damage = hurricane_data['Damage']

        if damage != 'Damages not recorded':
            # Convert damage to float value
            damage_value = float(damage[:-1]) if damage.endswith('B') else float(damage[:-1]) * 1_000_000
        else:
            damage_value = 0

        for rating, upper_bound in damage_scale.items():
            if damage_value <= upper_bound:
                hurricanes_by_damage[rating].append({
                    'Name': hurricane_data['Name'],
                    'Month': hurricane_data['Month'],
                    'Year': hurricane_data['Year'],
                    'Max Sustained Wind': hurricane_data['Max Sustained Wind'],
                    'Areas Affected': hurricane_data['Areas Affected'],
                    'Damage': damage_value,
                    'Deaths': hurricane_data['Deaths']
                })
                break

    return hurricanes_by_damage

# Damage scale
damage_scale = {0: 0, 1: 100_000_000, 2: 1_000_000_000, 3: 10_000_000_000, 4: 50_000_000_000}

# Example usage
hurricanes_by_damage = rate_hurricanes_by_damage(hurricanes_data, damage_scale)

# Print the hurricanes for each damage rating
for rating, hurricanes_list in hurricanes_by_damage.items():
    print(f"\nDamage Rating {rating}:")
    for hurricane in hurricanes_list:
        print(hurricane)
