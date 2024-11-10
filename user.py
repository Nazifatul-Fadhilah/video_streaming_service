

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
  list_plan = ["Basic Plan","Standard Plan","Premium Plan"]
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

  def check_user_plan(self):
    """
    Fungsi untuk menampilkan plan dan benefit dari current plan user
    """

    if (self.current_plan):
      print(f"{self.username} sedang berlangganan {self.current_plan}")
      print("Benefit yang didapatkan")

      idx_current_plan = self.list_plan.index(self.current_plan) #digunakan untuk menemukan posisi (indeks) dari nilai self.current_plan di dalam daftar self.list_plan.
      headers_user = [self.headers[idx_current_plan],self.headers[-1]]
      table_user = [[ row[idx_current_plan],row[-1]]
                        for row in self.list_benefit]
      # print(tabulate(table_user,headers_user))
      print(headers_user,table_user)

    else:
      print("anda belum berlangganan")

  def upgrade_plan(self,new_plan):
    """
    Fungsi untuk melakukan upgrade plan baru

    input: new_plan (str)
    """
    if (self.current_plan is not None and new_plan in self.list_plan):
      idx_current_plan = self.list_plan.index(self.current_plan)
      idx_new_plan = self.list_plan.index(new_plan)
      if (idx_new_plan > idx_current_plan):
        #Do Upgrade
        if(self.duration_plan > 12):
          # mendapatkan diskon
          total = self.list_benefit[-1][idx_new_plan] - 0.05 *self.list_benefit[-1][idx_new_plan]
        else:
          # harga tetap
          total = self.list_benefit[-1][idx_new_plan]
        print(f'Harga upgrade ke {new_plan} adalah Rp.{total:,}')

        # Upgrade data user
        self.current_plan = new_plan
        for key,value in self.data_user.items():
          if value[0] == self.username:
            self.data_user[key][1] = new_plan # akses data lalu ubah value
            break

      elif (idx_new_plan == idx_current_plan):
        print(f'Anda sedang berlangganan {new_plan}')
      else:
        print(f"Anda tidak bisa downgrade ke {new_plan}")

    elif(new_plan not in self.list_plan):
      print(f'New plan tidak tersedia')
    
    elif(self.current_plan is None):
      print(f'Silahkan berlangganan terlebih dahulu')

  def subs_plan(self,plan,kode_referral):
    """
    Fungsi untuk melakukan subscibe plan bagi user baru

    input:
      - plan(str)
      - kode_referral(str)
    """

    if(self.current_plan is None):
      if (plan in self.list_plan):
        list_code = [row[-1] for row in self.data_user.values()]
        # do subs
        self.current_plan = plan
        self.duration_plan = 1
        self.kode_referral = f"{self.username}-123"

        idx_plan = self.list_plan.index(plan)
        # menampilkan harga
        if (kode_referral in list_code):
          # dapat diskon
          total = self.list_benefit[-1][idx_plan] - 0.04 * self.list_benefit[-1][idx_plan]
        
        #  harga normal
        else:
          total = self.list_benefit[-1][idx_plan]
        print(f'Harga yang harus dibayarkan untuk subs {plan} adalah Rp. {total:,}')

        # tambahkan user baru
        last_key = max(self.data_user.keys())
        self.data_user[last_key+1] = [self.username,self.current_plan,self.duration_plan,self.kode_referral]

      else:
        print(f'Plan tidak tersedia')
    else:
      print("Anda sudah memiliki plan")
    
   

 


       
  
