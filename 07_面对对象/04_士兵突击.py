class Gun:
    def __init__(self, model):
        self.model = model

        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("请先裝填子弹")
            return
        self.bullet_count -= 1
        print("pa,shoot success!!")
        print("%s shooting 1 bullet" % self.model)
        print("%s left %d bullets" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def add_bullet(self, count):
        self.gun.bullet_count += count
        print("%s adding %d bullets" % (self.gun.model, count))


andy = Soldier("andy", Gun("AK47"))
andy.add_bullet(40)
andy.gun.shoot()
