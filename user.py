

# from tabulate import tabulate

class User:
  # Data user
  data_user = {
    1: ["Shandy","Basic Plan", 12, "shandy-2134"],
    2: ["Cahya","Standard Plan", 24, "cahya-abcd"],
    3: ["Ana","Premium Plan", 5, "ana-2f9g"],
    4: ["Bagus","Basic Plan", 11, "bagus-9f92"]
  }
  # data list_plan
  list_plan = ["Basic Plan","Standar Plan","Premium Plan"]
  list_benefit = [[True, True, True, "Bisa Stream"],
                 [True, True, True, "Bisa Download"],
                 [True, True, True, "Kualitas SD"],
                 [False, True, True, "Kualitas HD"],
                 [False, False, True, "Kualitas UHD"],
                 [1, 2, 4, "Number of Devices"],
                 ["3rd party Movie only", "Basic Plan Content + Sports", "Basic Plan + Standard Plan + PacFlix Original Series", "Jenis Konten"],
                 [120_000, 160_000, 200_000, "Harga"]]
  headers = ["Basic Plan", "Standard Plan", "Premium Plan", "Services"]

  def __init__(self, username):
    """
    Fungsi ini digunakan untuk menginisiasi objek user

    input: username (str)
    
    """

    self.username = username
    self.current_plan = None
    self.duration_plan = None
    self.kode_referal = None

    for key,value in self.data_user.items():
      if value[0] == self.username:
        self.current_plan = value[1]
        self.duration_plan = value[2]
        self.kode_referal = value[3]
        break

  def check_all_plan(self):
    """
      Fungsi ini digunakan untuk mencetak plan dan benefit

      input: None
    """
    print("List Benefit and Plan from Pacflix")
    print("")
    # print(tabulate(self.list_benefit,self.header))
    print(self.headers)
    print(self.list_benefit)


       
  
