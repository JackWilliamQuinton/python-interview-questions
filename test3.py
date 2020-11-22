def similar_license_plates(plate1, plate2):
    shape_dict = {"1": ["1", "I", "T"],
                  "0": ["0", "O", "Q"],
                  "Z": ["Z", "2"],
                  "S": ["S", "5"],
                  "8": ["8", "B"]
                  }

    def convert_plate(plate):
        plate = plate.replace(" ", "")
        for index, char in enumerate(plate):
            for key, item in shape_dict.items():
                if char in item:
                    plate = plate.replace(plate[index], key)
        return (plate)

    if convert_plate(plate1) == convert_plate(plate2):
        return True
    else:
        return False