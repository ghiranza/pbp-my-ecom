checklist Tugas 2:

(1) Membuat sebuah proyek Django baru 
    = django-admin startproject <project name>
      ^menjalankan perintah di atas pada terminal, 
       dalam kasus saya, project name nya adalah "pbp my ecom"

(2) Membuat aplikasi dengan nama main pada proyek tersebut
    = python manage.py startapp main
      ^menjalankan perintah di atas pada terminal,
      
(3) Melakukan routing pada proyek agar dapat menjalankan aplikasi main
    = INSTALLED_APPS = [
        ...
        'main'
      ]
      ^menambahkan aplikasi main ke dalam file settings.py
    = urlpatterns = [
        ...
        path('', include('main.urls'))
      ]
      ^menambahkan routing aplikasi main pada file urls.py
      
(4) Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut: - name
                                                                                                     - price
                                                                                                     - description
    = class Product(models.Model):
        name = models.CharField()
        price = models.IntegerField()
        description = models.TextField()
        bonus = models.IntegerField()

(5) Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu
    = def show_main(request) {
        context = {
        'nama':'Ghiranza Athaya Hamid'
        'kelas':'PBP A'
        ...
        }
      }
      
(6) Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
    = urlpatterns = [
        path('', views.info, name='info')
      ]

(7) Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet
    ^belum bisa melakukan deployment ke PWS



jawaban pertanyaan-pertanyaan Tugas 2:
(1) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
    = Saya memulai dengan melakukan Tutorial: Instalasi Django dan Inisiasi Proyek Django (Tutorial 0), namun saya membedakan nama-namanya. 
      Saya membuat file baru pada komputer lokal saya yang bernama "pbp my ecom", kemudian membuat virtual environment.
      Lalu, saya membuat file requirements.txt, menjalankan virtual environment, dan membuat proyek bernama pbp_my_ecom.

(2) Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan 
    jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
    = 

(3) Jelaskan fungsi git dalam pengembangan perangkat lunak!
    = Git berfungsi sebagai sistem kontrol versi (version system control) yang membantu pengembang menyimpan, mengelola source code, serta
      berkolaborasi dengan tim dengan efisien.

(4) Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    = Setau saya karena Django merupakan framework yang menggunakan bahasa Python sehingga cocok untuk pemula 
