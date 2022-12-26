fin, fout = open('promote.in', 'r'), open('promote.out', 'w')


bronze = fin.readline().strip()
silver = fin.readline().strip()
gold = fin.readline().strip()
plat = fin.readline().strip()

diff_bronze = int(bronze.split()[0]) - int(bronze.split()[1])
diff_silver = int(silver.split()[0]) - int(silver.split()[1])
diff_gold = int(gold.split()[0]) - int(gold.split()[1])
diff_plat = int(plat.split()[0]) - int(plat.split()[1])

fout.write(f'{abs(diff_silver + diff_gold + diff_plat)}\n')
fout.write(f'{abs(diff_gold + diff_plat)}\n')
fout.write(f'{abs(diff_plat)}\n')

