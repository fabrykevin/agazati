

from fuctions import getContinents, readFile,writeContinentsToFile, writeCompetitorsFromCountryToFile , writeTotalPointsToFile


readFile()
print(getContinents())
writeContinentsToFile(getContinents())


code=input('Kérem az ország kódját: ')
writeCompetitorsFromCountryToFile(code)

writeTotalPointsToFile()