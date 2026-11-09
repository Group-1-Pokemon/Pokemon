import random
import time

#bang tuong khac he
TYPE_CHART = { "Fire": {"Fire": 0.5, "Grass": 1.5, "Water": 0.5},
                "Grass": {"Fire": 0.5, "Grass": 0.5, "Water": 1.5},
                "Water": {"Fire": 1.5, "Grass": 0.5, "Water": 0.5},
                "Normal": {"Fire": 1, "Grass": 1, "Water": 1} }
    
class Pokemon():

    def __init__(self, name, hp, atk, element, moves):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
        self.element = element
        self.moves = list(moves) #danh sach chieu thuc
        self.level = 5 #level ban dau
        self.exp = 0
        self.max_exp = 100 #exp ban dau can de len level tiep theo
    
    def is_alive(self): #ham kiem tra trang thai con song hay khong
        return self.hp > 0
    
    def attack(self, opponent, move): #ham tan cong tinh toan sat thuong gay ra va nhan vao
        base_damage = move.damage + int(self.atk * 0.2)
        damage = random.randint(base_damage - 3, base_damage + 3)
        real_damage = int(damage * TYPE_CHART.get(move.element, {}).get(opponent.element, 1))
        real_damage = max(1, real_damage)
        if random.random() < 0.1:
            opponent.hp -= int(real_damage * 1.25)
            opponent.hp = max(0, opponent.hp)
            print("CHÍ MẠNG!")
        else:
            opponent.hp -= real_damage
            opponent.hp = max(0, opponent.hp)
        
        if TYPE_CHART.get(move.element, {}).get(opponent.element, 1) > 1:
            print(f"{self.name} dùng chiêu {move.name} tấn công {opponent.name} gây ra {real_damage} sát thương siêu hiệu quả!")
            
        elif TYPE_CHART.get(move.element, {}).get(opponent.element, 1) < 1:
            print(f"{self.name} dùng chiêu {move.name} tấn công {opponent.name} gây ra {real_damage} sát thương kém hiệu quả")
            
        else:
            print(f"{self.name} dùng chiêu {move.name} tấn công {opponent.name} gây ra {real_damage} sát thương")
        time.sleep(1)
        
    def gain_exp(self, amount): #ham tinh toan kinh nghiem va len level
        self.exp += amount
        print(f"- Bạn đã nhận được {amount} kinh nghiệm! (Tiến trình {self.exp}/{self.max_exp}) -")
        
        while self.exp >= self.max_exp:
            self.exp = self.exp - self.max_exp
            self.level += 1
            self.max_exp = int(self.max_exp * 1.25)
            print(f"- {self.name} đã tăng lên cấp {self.level} -")
            
            self.max_hp += random.randint(10,15)
            self.hp = self.max_hp
            self.atk += random.randint(3, 7)
            print("- Sức mạnh của Pokemon đã tăng lên! -") #tang chi so khi len level
        time.sleep(0.5)
    
    #ham tien hoa 
    def evolve(self): 
        old_name = self.name
        if self.level >= 10:
            
            if self.name == "Charmander":
                self.name = "Charmeleon"
                new_move = Move("Fire Fang", 50, "Fire")
                self.moves.append(new_move)
                self.atk = self.atk + 12
                self.max_hp = self.max_hp + 20
                self.hp = self.max_hp
                print(f"-- Chúc mừng bạn! {old_name} đã tiến hóa thành {self.name} --")
                time.sleep(0.5)
                print(f"Pokemon đã học được chiêu mới: {new_move.name}")
                time.sleep(0.5)
                print(f"- Sức mạnh của bạn đã tăng lên đáng kể! -")
                time.sleep(0.5)
                
            if self.name == "Bulbasaur":
                self.name = "Ivysaur"
                new_move = Move("Razor Leaf", 50, "Grass")
                self.moves.append(new_move)
                self.atk = self.atk + 11
                self.max_hp = self.max_hp + 22
                self.hp = self.max_hp
                print(f"-- Chúc mừng bạn! {old_name} đã tiến hóa thành {self.name} --")
                time.sleep(0.5)
                print(f"Pokemon đã học được chiêu mới: {new_move.name}")
                time.sleep(0.5)
                print(f"- Sức mạnh của bạn đã tăng lên đáng kể! -")
                time.sleep(0.5)
                
            if self.name == "Squirtle":
                self.name = "Wartortle"
                new_move = Move("Water Pulse", 50, "Water")
                self.moves.append(new_move)
                self.atk = self.atk + 10
                self.max_hp = self.max_hp + 24
                self.hp = self.max_hp
                print(f"-- Chúc mừng bạn! {old_name} đã tiến hóa thành {self.name} --")
                time.sleep(0.5)
                print(f"Pokemon đã học được chiêu mới: {new_move.name}")
                time.sleep(0.5)
                print(f"- Sức mạnh của bạn đã tăng lên đáng kể! -")
                time.sleep(0.5)
                
        if self.level >= 20:
            
            if self.name == "Charmeleon":
                self.name = "Charizard"
                new_move = Move("Flamethrower", 70, "Fire")
                self.moves.append(new_move)
                self.atk = self.atk + 20
                self.max_hp = self.max_hp + 30
                self.hp = self.max_hp
                print(f"-- Chúc mừng bạn! {old_name} đã tiến hóa thành {self.name} --")
                time.sleep(0.5)
                print(f"Pokemon đã học được chiêu mới: {new_move.name}")
                time.sleep(0.5)
                print(f"- Sức mạnh của bạn đã tăng lên đáng kể! -")
                time.sleep(0.5)
                
            if self.name == "Ivysaur":
                self.name = "Venusaur"
                new_move = Move("Solar Beam", 70, "Grass")
                self.moves.append(new_move)
                self.atk = self.atk + 17
                self.max_hp = self.max_hp + 33
                self.hp = self.max_hp
                print(f"-- Chúc mừng bạn! {old_name} đã tiến hóa thành {self.name} --")
                time.sleep(0.5)
                print(f"Pokemon đã học được chiêu mới: {new_move.name}")
                time.sleep(0.5)
                print(f"- Sức mạnh của bạn đã tăng lên đáng kể! -")
                time.sleep(0.5)
                
            if self.name == "Wartortle":
                self.name = "Blastoise"
                new_move = Move("Water Cannon", 70, "Water")
                self.moves.append(new_move)
                self.atk = self.atk + 14
                self.max_hp = self.max_hp + 36
                self.hp = self.max_hp
                print(f"-- Chúc mừng bạn! {old_name} đã tiến hóa thành {self.name} --")
                time.sleep(0.5)
                print(f"Pokemon đã học được chiêu mới: {new_move.name}")
                time.sleep(0.5)
                print(f"- Sức mạnh của bạn đã tăng lên đáng kể! -")
                time.sleep(0.5)
        
class Move(): #ham chieu thuc cua Pokemon
    def __init__(self, name, damage, element):
        self.name = name
        self.damage = damage
        self.element = element
          
def heal(pokemon): #ham hoi mau trong tran dau
    heal_amount = random.randint(40,50)
    pokemon.hp += heal_amount
    if pokemon.hp > pokemon.max_hp:
        pokemon.hp = pokemon.max_hp
    print(f"{pokemon.name} đã được hồi {heal_amount} máu")

def battle(player_pokemon): #ham tran dau giua 2 Pokemon
    
    #chieu thuc cua Pokemon hoang da
    move11 = Move("Tackle", 25, "Normal")
    move22 = Move("Amber", 30, "Fire")
    move33 = Move("Leaf Blade", 30, "Grass")
    move44 = Move("Bubble", 30, "Water")
    
    #danh sach doi thu
    enemy = [ {"name": "Charmander", "hp": 50, "atk": 15, "element": "Fire", "moves": [move11, move22]},
              {"name": "Bulbasaur", "hp": 55, "atk": 12, "element": "Grass", "moves": [move11, move33]},
              {"name": "Squirtle", "hp": 60, "atk": 10, "element": "Water", "moves": [move11, move44]} ]
        
    poke_spawn = random.choice(enemy)
    opponent_pokemon = Pokemon(poke_spawn["name"], poke_spawn["hp"], poke_spawn["atk"], poke_spawn["element"], poke_spawn["moves"])
    time.sleep(1)
    
    print(f"Bắt gặp một {opponent_pokemon.name} hoang dã!")
    print(f"{player_pokemon.name} xuất chiến!")
    
    while player_pokemon.is_alive() and opponent_pokemon.is_alive():
        
        print(f"{player_pokemon.name}: {player_pokemon.hp}/{player_pokemon.max_hp} vs {opponent_pokemon.name}: {opponent_pokemon.hp}/{opponent_pokemon.max_hp}")
        
        print("1. Tấn công")
        print("2. Hồi máu")
        print("3. Bỏ chạy")
        choice = input("Hành động tiếp theo của bạn là (Chọn một số từ 1-3): ")
        
        #lua chon hanh dong tan cong
        if choice == "1":
            #chon chieu thuc cho Pokemon   
            for index, move in enumerate(player_pokemon.moves, start = 1):
                print(f"{index}. {move.name}: Sát thương {move.damage} hệ {move.element}")
            move_choice = int(input(f"Chọn chiêu cho {player_pokemon.name} (Chọn một số từ 1-{len(player_pokemon.moves)}): ")) - 1
            selected_move = player_pokemon.moves[move_choice]
                
            
            if selected_move:
                if random.random() < 0.05: #Pokemon co the ne tranh tan cong
                    print(f"{opponent_pokemon.name} đã né được đòn tấn công của bạn")
                else:
                    player_pokemon.attack(opponent_pokemon, selected_move)
            time.sleep(1)
            if opponent_pokemon.is_alive():
                if random.random() < 0.05: #Pokemon co the ne tranh tan cong
                    print(f"Bạn đã né được đòn tấn công của {opponent_pokemon.name}")
                else:
                    enemy_move = random.choice(opponent_pokemon.moves)
                    opponent_pokemon.attack(player_pokemon, enemy_move)
            else:
                amount = random.randint(30,50)
                player_pokemon.gain_exp(amount)
                player_pokemon.evolve()
                print(f"Bạn đã hạ gục được {opponent_pokemon.name}!")
                if random.random() < 0.3:
                    player_pokemon.hp = player_pokemon.max_hp
                    print("Bạn gặp trạm y tế và được hồi phục!")
                return True
                
        #lua chon hanh dong hoi mau
        elif choice == "2":
            heal(player_pokemon)
            time.sleep(1)
            enemy_move = random.choice(opponent_pokemon.moves)
            opponent_pokemon.attack(player_pokemon, enemy_move)
        
        #lua chon hanh dong bo chay
        elif choice == "3":
            if random.random() < 0.7:
                print("Bạn đã chạy thoát thành công!")
                if random.random() < 0.3:
                    player_pokemon.hp = player_pokemon.max_hp
                    print("Bạn gặp trạm y tế và được hồi phục!")
                return False
            else:
                print("Bỏ chạy thất bại")
                enemy_move = random.choice(opponent_pokemon.moves)
                opponent_pokemon.attack(player_pokemon, enemy_move)
                time.sleep(1)
    return False
        
def main():
    #chieu thuc 
    move1 = Move("Tackle", 25, "Normal")
    move2 = Move("Amber", 30, "Fire")
    move3 = Move("Leaf Blade", 30, "Grass")
    move4 = Move("Bubble", 30, "Water")
    
    trainer_name = input("Nhập tên của bạn: ")
    if not trainer_name:
        trainer_name = "Unknown"
    print(f"==== Chào mừng {trainer_name} đến với cuộc phiêu lưu cùng Pokemon! ====")
        
    while True:
    
        Charmander = Pokemon("Charmander", 70, 15, "Fire", [move1, move2])
        Bulbasaur = Pokemon("Bulbasaur", 75, 12, "Grass", [move1, move3])    
        Squirtle = Pokemon("Squirtle", 80, 10, "Water", [move1, move4])
    
        #chọn Pokemon khởi đầu 
        print("Hãy chọn bạn đồng hành của bạn:")
        print("1. Charmander")
        print("2. Bulbasaur")
        print("3. Squirtle")
        choice = input("Lựa chọn của bạn (Chọn một số từ 1-3): ")

        if choice == "1":
            player_pokemon = Charmander
            print(f"---! {player_pokemon.name} đã trở thành bạn đồng hành của bạn! !---")
    
        elif choice == "2":
            player_pokemon = Bulbasaur
            print(f"---! {player_pokemon.name} đã trở thành bạn đồng hành của bạn! !---")
        
        elif choice == "3":
            player_pokemon = Squirtle
            print(f"---! {player_pokemon.name} đã trở thành bạn đồng hành của bạn! !---")
        
        else:
            player_pokemon = Charmander
            print("---! Bạn chọn sai nên Charmander sẽ trở thành bạn đồng hành của bạn !---")
        
        while player_pokemon.is_alive():
            print("...Bạn đang băng qua khu rừng...")
            time.sleep(1)
            if battle(player_pokemon):
                print("...Bạn tiếp tục hành trình của mình...")
            if not player_pokemon.is_alive():
                print("~- Pokemon của bạn đã gục ngã -~")
                break
            
        con_tinue = input("Bạn có muốn bắt đầu lại không? (1. Có | 2. Không) ")
        if con_tinue != "1":
            print("Hẹn gặp lại bạn!")
            break
    
if __name__ == "__main__":
    main()
    
    
    