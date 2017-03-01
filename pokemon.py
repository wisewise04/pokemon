from classes import Trainer, Pokemon,Hospital

print("안뇽 포켓몬월드로 gogo")

playername = input("플레이어 이름을 입력해 주세요:")
which_pokemon = input("시작하 포켓몬을 골라주세요[피카츄/동연몬/파이리/이상해씨")
if which_pokemon=="피카츄":
	pokemon = Pokemon("피카츄",25,10,1,"라이츄")
elif which_pokemon=="파이리":
	pokemon = Pokemon("파이리",25,10,1,"리자드")
elif which_pokemon=="동연몬":
	pokemon = Pokemon("동연몬",25,10,1,"동동연몬")
elif which_pokemon=="이상해씨":
	pokemon = Pokemon("이상해씨",25,10,1,"이상해풀")
else:
	print("잘못 입력해주셨네요, 내맘대로 로 시작합니다.")
	pokemon = Pokemon("피카츄",25,10,1,"라이츄")
trainer = Trainer(playername,pokemon)

print(trainer.pokemon_list[0].name)

