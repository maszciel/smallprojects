def tile():
    while True:
        try:
            tile_a = float(input("Tile area (cm2): "))
            tile_c = float(input("Cost of one tile ($): "))
            floor_w = float(input("Floor width (cm): "))
            floor_h = float(input("Floor height (cm): "))
        except:
            print("Wrong input.")
        else:
            break
    
    return floor_w * floor_h / tile_a * tile_c

if __name__ == "__main__":
    cost = tile()
    print(f"Total cost: {round(cost,2)}")
