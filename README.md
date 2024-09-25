<details>
  <summary>TUGAS 2</summary>
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
</details>



<details>
  <summary>TUGAS 4</summary>

checklist Tugas 4:
1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
   a) Penambahan import UserCreationForm [views.py], lalu menambahkan fungsi register [views.py]:
 ```python
 def register(request):
  form = UserCreationForm()

  if request.method == "POST":
      form = UserCreationForm(request.POST)
      if form.is_valid():
          form.save()
          messages.success(request, 'Your account has been successfully created!')
          return redirect('main:login')
  context = {'form':form}
  return render(request, 'register.html', context)
 ```
   b) Pembuatan berkas HTML baru dengan nama register.html pada main/templates yang berisi kode seperti berikut:
```python
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```
   c) Import fungsi register ke urls.py dan tambahkan path ke urlpatterns
   
   **PEMBUATAN FUNGSI LOGIN**
   d) Menambahkan import authenticate, login, dan AuthenticationForm [views.py]
   e) Menambahkan fungsi login_user [views.py] 
   f) Membuat berkas HTML baru dengan nama login.html pada main/templates yang berisi kode seperti berikut:
```python
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
   g) Import fungsi login_user ke urls.py dan tambahkan path ke urlpatterns

   **PEMBUATAN FUNGSI LOGOUT**
   h) Menambahkan import logout [views.py]
   i) Menambahkan fungsi logout_user [views.py]
   j) Menambahkan kode berikut pada main.html:
```python
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```
   k) Import fungsi logout_user ke urls.py dan tambahkan path ke urlpatterns

2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
   Membuat akun di form register lalu mengisi seluruh field yang dibutuhkan
   
3. Menghubungkan model Product dengan User
   a) Menambahkan kode berikut [models.py]:
```python
from django.contrib.auth.models import User
```
   b) Menambahkan kode berikut pada class VBucksEntry:
```python
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
   c) Mengubah isi create_vbcuks_entry [views.py]
   d) Mengubah beberapa isi dari show_main menjadi seperti berikut:
```python
    mood_entries = MoodEntry.objects.filter(user=request.user)

    context = {
         'name': request.user.username,
```
   e) Menambahkan import os [settings.py] dan mengganti variabel DEBUG dengan kode berikut:
```python
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```
4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi
   a) Menambahkan import HttpResponseRedirect, reverse, dan datetime
   b) Menambahkan cookie yang bernama last_login dengan cara mengubah kode if form.is_valid() menjadi sebagai berikut:
```python
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```

   c) Tambahkan kode berikut pada variabel context pada show_main
```python
'last_login': request.COOKIES['last_login'],
```
   d) Mengubah fungsi logout_user menjadi seperti berikut:
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
   e) Menambahkan kode berikut pada main.html:
```python
<h5>Sesi terakhir login: {{ last_login }}</h5>
```

jawaban pertanyaan-pertanyaan Tugas 4:
1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
   - HttpResponseRedirect(): bagian dari modul django.http, memberitahu browser bahwa URL sementara dialihkan ke URL lain
   - redirect(): disediakan Django dalam modul django.shortcuts, berfungsi menerima lebih dari satu jenis argumen, lebih sederhana

2. Menambahkan kode import ```from django.contrib.auth.models import User```, lalu menambahkan kode berikut pada class VBucksEntry: ```user = models.ForeignKey(User, on_delete=models.CASCADE)```, kemudian mengubah isi create_vbcuks_entry dan mengubah beberapa isi dari show_main menjadi seperti berikut:
```
    mood_entries = MoodEntry.objects.filter(user=request.user)

    context = {
         'name': request.user.username,
```

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
   - Authentication: proses verifikasi identitas pengguna 
   - Authorization: menentukan apakah pengguna yang telah terautentikasi memiliki izin untuk akses
Yang dilakukan saat pengguna login adalah Authentication. Authentication dilaksanakan terlebih dahulu untuk mengecek apakah data pengguna sesuai dengan data yang ada pada database, baru setelah itu melakukan proses authorization.
Django memiliki sistem authentication bawaan menggunakan model user, yaitu authenticate().
Django mengendalikan otorisasi dengan menggunakan permission dan group, yaitu @permission_required.

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Dengan penggunaan cookies. Django mengingat pengguna yang telah login menggunakan session yang disimpan di cookies dengan cara menyimpan session ID di cookies di browser pengguna.
Kegunaan lain dari cookies selain untuk mengelola sesi login adalah untuk menyimpan preferensi pengguna dan data-data lain yang diperlukan untuk meningkatkan pengalaman pengguna.
Meskipun cookies berguna, namun tIdak semua cookies aman. Keamanan cookies berrgantung pada bagaimana diimplementasikannya dan apakah pengaturan keamanan yang benar telah digunakan.

</details>
