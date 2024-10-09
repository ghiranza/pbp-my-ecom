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



<details>
  <summary>TUGAS 5</summary>

checklist Tugas 5:
1. Implementasikan fungsi untuk menghapus dan mengedit product
  a) Membuat fungsi baru bernama delete_vbucks [views.py], lalu import fungsi tersebut pada urls.py dan menambahkan path url pada urlpatterns
```pyhton
def delete_vbucks(request, id):
    vbucks = VBucksEntry.objects.get(pk = id)
    vbucks.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```
  b) Menambahkan kode berikut berupa tombol untuk delete product:
```python
<a href="{% url 'main:delete_vbucks' vbucks_entry.pk %}">
    <button>
        Delete
    </button>
</a>
```
  c) Membuat fungsi baru bernama edit_vbucks [views.py], lalu import fungsi tersebut pada urls.py dan menambahkan path url pada urlpatterns
```python
def edit_vbucks(request, id):
  mood = VBucksEntry.objects.get(pk = id)
  form = VBucksEntryForm(request.POST or None, instance=vbucks)
  if form.is_valid() and request.method == "POST":
  form.save()
  return HttpResponseRedirect(reverse('main:show_main'))
  context = {'form': form}
  return render(request, "edit_vbucks.html", context)
```
  c2) Menambahkan import file reverse dan HttpResponseRedirect
  c3) Membuat edit_vbucks.html pada main/templates yang berisi kode berikut:
```python
<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Edit Mood"/>
      </td>
    </tr>
  </table>
</form>
```
  d) Menambahkan potongan kode berikut pada main.html
```python
<a href="{% url 'main:edit_mood' mood_entry.pk %}">
  <button>
    Edit
  </button>
</a>
```
2. Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
- Ketentuan 1: Kustomisasi halaman login, register, dan tambah product semenarik mungkin
  ^saya menjalankan ketentuan di atas dengan menambahkan kotak atau semacam box yang menjadi frame elemen-elemen pada halaman web
   saya juga mengubah warna dengan membuat halaman web seakan dalam "dark mode"
   contohnya adalah pada gambar berikut: ![tugas 5](https://github.com/user-attachments/assets/00149e0f-ea1d-4b83-a446-5ebf9f94778c)
- Ketentuan 2: Kustomisasi halaman daftar product menjadi lebih menarik dan responsive, dengan kondisi -> Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar
                                                                                                       -> Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card
  ^saya meng-custom halaman daftar product dengan cara mengubah warna web menjadi "dark mode", serta memberi warna biru gradasi pada tombol
   contohnya seperti gambar berikut: ![tugas 5 (2)](https://github.com/user-attachments/assets/b4869e56-b588-40e9-9ea0-f4405fe33ff2)
   jika belum ada product yang tersimpan, maka halaman di web akan menampilkan: ![tugas 5 (3)](https://github.com/user-attachments/assets/c1dedc32-d905-4ae3-a844-6b3ecbbc13fa)
   dan jika product sudah tersimpan, product akan ditampilkan menggunakan card seperti: ![tugas 5 (4)](https://github.com/user-attachments/assets/7866fc3a-dd30-4ff2-95a0-842f7f534113)
- Ketentuan 3: Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
  ^saya membuat kedua button pada card product tersebut dengan kode di bawah ini:
```python
<div class="absolute top-0 -right-4 flex space-x-1">
    <a href="{% url 'main:edit_vbucks' vbucks_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
            <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
        </svg>
    </a>
    <a href="{% url 'main:delete_vbucks' vbucks_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
        </svg>
    </a>
</div>
```
   kode ini juga menempatkan kedua button tersebut pada atas kanan card product
   berikut gambarnya: ![tugas 5 (5)](https://github.com/user-attachments/assets/a042a8d8-24d5-4630-8a48-e38f470cd937)
- Ketentuan 4: Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
   ^untuk mobile, berikut kode saya untuk mengimplementasikan perintah di atas:
```python
<div class="mobile-menu hidden md:hidden px-4 w-full md:max-w-full">
  <div class="pt-2 pb-3 space-y-1 mx-auto">
    <a href="#" class="block text-gray-300 px-3 py-2">Home</a>
    <a href="#" class="block text-gray-300 px-3 py-2">Products</a>
    <a href="#" class="block text-gray-300 px-3 py-2">Categories</a>
    <a href="#" class="block text-gray-300 px-3 py-2">Cart</a>
   
    {% if user.is_authenticated %}
      <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
      <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
        Logout
      </a>
    {% else %}
      <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
        Login
      </a>
      <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
        Register
      </a>
    {% endif %}
  </div>
</div>
<script>
  const btn = document.querySelector("button.mobile-menu-button");
  const menu = document.querySelector(".mobile-menu");

  btn.addEventListener("click", () => {
    menu.classList.toggle("hidden");
  });
</script>
```
   sedangkan untuk mode desktop, berikut kodenya:
```python
<nav class="bg-gray-800 shadow-lg fixed top-0 left-0 z-40 w-full">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <div class="flex items-center">
        <h1 class="text-2xl font-bold text-left text-white">V-Bucks Store</h1>
      </div>
     
      <div class="flex space-x-8">
        <a href="#" class="text-white text-sm font-medium hover:text-gray-300">Home</a>
        <a href="#" class="text-white text-sm font-medium hover:text-gray-300">Products</a>
        <a href="#" class="text-white text-sm font-medium hover:text-gray-300">Categories</a>
        <a href="#" class="text-white text-sm font-medium hover:text-gray-300">Cart</a>
      </div>
     
      <div class="hidden md:flex items-center">
        {% if user.is_authenticated %}
          <span class="text-gray-300 mr-4">Welcome, {{ user.username }}</span>
          <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Logout
          </a>
        {% else %}
          <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">
            Login
          </a>
          <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Register
          </a>
        {% endif %}
      </div>
      <div class="md:hidden flex items-center">
        <button class="mobile-menu-button">
          <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
            <path d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
        </button>
      </div>
    </div>
  </div>
</nav>
```
   dan juga berikut lampirannya: ![tugas 5 (6)](https://github.com/user-attachments/assets/f6527af8-b05e-4299-9b4b-f8ab0bf948de)

pertanyaan-pertanyaan Tugas 5:
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
= - !important (dengan inline style paling tinggi): jika suatu aturan CSS ditandai dengan !important, maka semua aturan lainnya akan disampingkan
  - Inline styles (dalam elemen HTML): atribut style, misal ...style="color: red;"...
  - ID selectors: #, misal #example ...
  - Class, attribute, dan pseudo-class selectors: misal .example, [attr], dan :hover
  - Element dan pseudo-element selectors: misal div dan p, ::before dan ::after

3. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
= Penting karena memungkin tampilan web untuk menyesuaikan ukuran layar device yang berbeda-beda
  Aplikasi yang sudah menerapkan: Google
  Aplikasi yang belum menerapkan: Reddit (versi lama)
 
5. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
= Margin adalah jarak di luar elemen, pemisah suatu elemen dari elemen lain
  Border adalah garis yang mengelilingi elemen
  Padding adalah jarak antara konten elemen dan border
  Cara mengimplementasikan ketiganya adalah sepert: ...margin: 10px;..., ...border: 2px solid black;..., ...padding: 20px;...

7. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
= Flex box merupakan sistem layout **satu dimensi** yang mengatur elemen dalam baris atau kolom secara fleksibel, sedangkan grid layout merupakan sistem **dua dimensi** yang memungkinkan penempatan elemen dalam baris dan kolom secara lebih presisi.
  Flex box lebih cocok untuk navigasi sederhana karena mudah dan berguna untuk layout satu dimensi
  Grid layout cocok untuk struktur yang lebih kompleks, seperti layout dengan sidebar.
   
</details>



<details>
  <summary>TUGAS 6</summary>

checklist Tugas 6:
AJAX GET
1. Ubahlah kode cards data mood agar dapat mendukung AJAX GET.
= menambahkan potongan kode berikut untuk mengambil data dari server dan menampilkan entri secara dinamis tanpa reload halaman [main.html]:
```python
async function getVBucksEntries() {
    return fetch("{% url 'main:show_json' %}").then((res) => res.json())
}

async function refreshVBucksEntries() {
    document.getElementById("vbucks_entry_cards").innerHTML = "";
    const vbucksEntries = await getVBucksEntries();
    let htmlString = "";

    if (vbucksEntries.length === 0) {
        htmlString = `
            ...
        `;
    }
    else {
        vbucksEntries.forEach((item) => {
            const name = DOMPurify.sanitize(item.fields.name);
            const description = DOMPurify.sanitize(item.fields.description);
            htmlString += `
            ...
            `;
        });
    }
    document.getElementById("vbucks_entry_cards").className = classNameString;
    document.getElementById("vbucks_entry_cards").innerHTML = htmlString;
}
refreshVBucksEntries();
```

2. Lakukan pengambilan data mood menggunakan AJAX GET. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.
= menambahkan potongan kode berikut dalam fungsi show_json() untuk meng-filter berdasarkan pengguna yang sedang login [views.py]:
```python
def show_json(request):
    data = VBucksEntry.objects.filter(user=request.user) 
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

AJAX POST
1. Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan mood.
= menambahkan potongan kode berikut untuk menambahkan data mood baru melalui AJAX [main.html]"
```python
<button data-modal-target="crudModal" data-modal-toggle="crudModal" class="text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" style="background: linear-gradient(to right, #1B90DD, #5FCEEA);" onclick="showModal();">
    Add New VBucks Entry by AJAX
</button>
```

2. Buatlah fungsi view baru untuk menambahkan mood baru ke dalam basis data.
= menambahkan view baru add_vbucks_entry_ajax untuk menangani POST request dari form [views.py]:
```python
@csrf_exempt
@require_POST
def add_vbucks_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    bonus = request.POST.get("bonus")
    user = request.user

    new_vbucks = VBucksEntry(
        name=name, description=description,
        bonus=bonus,
        user=user
    )
    new_vbucks.save()

    return HttpResponse(b"CREATED", status=201)
```

3. Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.
= menambahkan path berikut dalam [urls.py]:
```pyhton
path('create-vbucks-entry-ajax', add_vbucks_entry_ajax, name='add_vbucks_entry_ajax'),
```

4. Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.
= menambahkan fungsi addVBucksEntry() yang mengirimkan data form ke path /create-vbucks-entry-ajax/ [main.html]:
```python
function addVBucksEntry() {
  fetch("{% url 'main:add_vbucks_entry_ajax' %}", {
    method: "POST",
    body: new FormData(document.querySelector('#vbucksEntryForm')),
  })
  .then(response => refreshVBucksEntries())

  document.getElementById("vbucksEntryForm").reset(); 
  document.querySelector("[data-modal-toggle='crudModal']").click();

  return false;
}
```

5. Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar mood terbaru tanpa reload halaman utama secara keseluruhan.
= pada fungsi addVBucksentry(), saya memanggil fungsi refreshVBucksEntries() untuk memperbarui daftar entri mood secara dinamis [main.html]. Berikut potongan kodenya:
```python
.then(response => refreshVBucksEntries())
```

pertanyaan-pertanyaan Tugas 6:
1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
= JavaScript memungkinkan fungsionalitas yang interaktif dan dinamis di dalam halaman web. JavaScript sangat bermanfaat karena dapat memperbarui dan mengubah HTML & CSS dengan cepat, menangani peristiwa user seperti klik dan pengiriman formulir, melakukan validasi data sisi klien, dan membuat permintaan asinkron ke server (AJAX), semuanya tanpa memuat ulang halaman. Sehingga, JavaScript membuat pengalaman pengguna yang lebih baik, interaksi yang lebih cepat, dan interaktivitas yang lebih baik.

2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
=  kata kunci **await** dalam fetch fetch() digunakan untuk menghentikan sementara eksekusi kode, hingga operasi fetch asinkron selesai dan mengembalikan hasil. jika tidak menggunakan **await**, kode akan terus dieksekusi saat permintaan fetch masih tertunda, menyebabkan data yang tidak lengkap atau tidak terdefinisi digunakan dalam operasi berikutnya.

3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
= csrf_exempt digunakan untuk mem-bypass proteksi CSRF untuk tampilan spesifik yang menangani permintaan AJAX POST. 

4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
= hanya mengandalkan validasi frontend itu tidak aman. Validasi frontend dapat dilewati atau dimanipulasi oleh user dengan penggunaan skrip berbahaya. Dengan memvalidasi dan membersihkan input di backend, kita memastikan bahwa hanya data yang aman dan valid yang mencapai logika inti dan database aplikasi kita.

</details>