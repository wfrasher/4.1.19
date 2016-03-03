



def pond(years, initialPopulation, harvest,restock):
    population = initialPopulation

    for year in range(years):
        population = 1.08 * population - harvest + restock
        print(year +1, int(population))


    return population





pond(15,12000,800,100)



# generalize to allow for the pond to be annually restocked with an additional quantity of fish