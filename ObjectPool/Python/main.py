from Pool import Pool

pool = Pool()

Object1 = pool.GetObject()
Object1.Print()
pool.ReleaseObject(Object1)
print('___________')


Object1 = pool.GetObject()
Object2 = pool.GetObject()
Object1.Print()
Object2.Print()
pool.ReleaseObject(Object1)
pool.ReleaseObject(Object2)
print('____________')

Object1 = pool.GetObject()
Object2 = pool.GetObject()
Object3 = pool.GetObject()
Object4 = pool.GetObject()
