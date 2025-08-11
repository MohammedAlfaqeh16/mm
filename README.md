# 📚 نظام إدارة مكتبة باستخدام Django

مشروع ويب بسيط واحترافي لإدارة مكتبة باستخدام إطار العمل **Django**، يسمح بإضافة الكتب، تسجيل المستخدمين، تسجيل الدخول، وتنظيم الواجهة باستخدام **Bootstrap 5** و**Font Awesome**.

---

## 🚀 المميزات

- 🔐 تسجيل الدخول والخروج وتسجيل المستخدمين الجدد
- 📖 إدارة الكتب (إضافة – عرض – تعديل – حذف)
- ⚙️ لوحة تحكم المسؤول عبر Django Admin
- 🎨 واجهة مستخدم متجاوبة باستخدام Bootstrap
- 🧠 إدارة الصلاحيات للمستخدمين
- 🌍 يدعم اللغة العربية

---

## 🧰 الأدوات والتقنيات المستخدمة

- [Django](https://www.djangoproject.com/) – لبناء التطبيق
- [Bootstrap 5](https://getbootstrap.com/) – لتنسيق وتصميم الواجهة
- [Font Awesome](https://fontawesome.com/) – لاستخدام الأيقونات
- [SQLite](https://www.sqlite.org/index.html) – قاعدة البيانات الافتراضية
- HTML / CSS / JavaScript

---

## 📸 صور من المشروع

> يمكنك إضافة صور لواجهة المستخدم هنا لاحقًا عند رفعها على المستودع أو باستخدام روابط مباشرة.
>
> <img width="1366" height="768" alt="‏‏لقطة الشاشة (46)" src="https://github.com/user-attachments/assets/5293453c-192c-4493-af0f-3615af7176ff" />


<img width="1366" height="768" alt="‏‏لقطة الشاشة (46)" src="https://github.com/user-attachments/assets/17bb2ec1-5ed0-4bff-80f5-a85fae62b4fa" />
<img width="1366" height="768" alt="‏‏لقطة الشاشة (46)" src="https://github.com/user-attachments/assets/8afe53b2-59bf-424c-93fc-e81a9cb1fe0e" />





---

## ⚙️ خطوات تشغيل المشروع

```bash
# 1. نسخ المستودع
git clone https://github.com/MohammedAlfaqeh16/mm.git
cd mm

# 2. إنشاء بيئة افتراضية
python -m venv venv
source venv/bin/activate   # على لينكس/ماك
venv\Scripts\activate      # على ويندوز

# 3. تثبيت المتطلبات
pip install -r requirements.txt

# 4. تنفيذ الترحيلات
python manage.py migrate

# 5. إنشاء مستخدم مسؤول
python manage.py createsuperuser

# 6. تشغيل الخادم المحلي
python manage.py runserver




📁 هيكل المشروع
library/
├── library/               # مجلد الإعدادات الرئيسي
│   ├── settings.py
│   └── urls.py
├── libraryApp/            # التطبيق الخاص بالمكتبة
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── static/
├── templates/             # القوالب العامة
├── static/                # ملفات CSS/JS
└── manage.py



👥 بيانات دخول افتراضية (اختياري)
اسم المستخدم	كلمة المرور	الدور
admin	admin123	مشرف عام
user	user123	مستخدم عادي




✅ المهام القادمة
 إضافة نظام استعارة الكتب

 تصفية الكتب حسب الفئة أو اللغة

 توليد تقارير PDF

 رفع المشروع إلى سيرفر (مثل: Heroku أو PythonAnywhere)




📬 معلومات التواصل
محمد الفقيه
📧 alfaqehm20@gmail.com
🔗 حساب GitHub

