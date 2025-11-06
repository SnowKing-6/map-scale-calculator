# Map Scale Calculator 📐🗺️

A small, practical desktop tool to calculate a map scale by entering the measured length on the map and the actual real-world length, with unit selection.

## ✨ Overview
This is a lightweight desktop utility built with customtkinter for a clean, modern UI. It calculates the map scale in the format "1 : X" by converting the real-world measurement to centimeters and computing the ratio automatically.

## ✅ Features
- Clean and easy-to-use graphical interface.
- Supports length units: centimeters (cm), meters (m), kilometers (km).
- Validates input and shows clear user messages on errors.
- Formats the resulting scale with thousands separators for readability.

## ⚠️ Important note about hectares
The unit "hectare" is included in the UI, but hectare is an area unit (not a linear length). Therefore, calculating a linear scale using hectares is not meaningful. If selected, the application will notify the user that the scale cannot be calculated with hectares.

## Requirements
- Python 3.8 or newer
- customtkinter library

To install the requirement:

```powershell
python -m pip install --upgrade pip
pip install customtkinter
```

## How to run (Windows PowerShell)
1. Open PowerShell in the project folder.
2. Run the script that contains the source code:

```powershell
python .\مقاييس الرسم.py
# or
py -3 .\مقاييس الرسم.py
```

3. The "Map Scale Calculator" window will open. Enter the measured length on the map (in cm), enter the real-world length, select the unit, and press "Calculate Scale".

## Quick example
- If the map measurement = 2 cm and the real-world length = 1 km
  - 1 km = 100,000 cm → scale = 100,000 / 2 = 1 : 50,000

## Input handling
- Values must be positive.
- Non-numeric input will trigger a friendly warning asking for valid numbers.

## Suggestions for future improvements
- Add support for selecting the unit of the map measurement (e.g., mm, in).
- Add an option to save or export the result (image/pdf).
- Add a graphical scale bar to visually represent the computed scale.

## License
This is a simple utility free to use and modify. If you prefer, you can add an explicit license (for example, MIT) to clarify reuse terms.

## Author
Creator: Razi Ramzi ✍️

For questions or improvement suggestions, feel free to reach out through your preferred channels.
# برنامج حساب مقياس الخريطة 📐🗺️

برنامج بسيط وعملي لحساب مقياس الخريطة من خلال إدخال طول المقاس على الخريطة وطول المقياس الحقيقي مع اختيار الوحدة.

## ✨ نظرة عامة
هذه أداة سطح مكتب مبنية باستخدام customtkinter لواجهة أنيقة وسهلة الاستخدام. تسمح لك بحساب مقياس الخريطة بصيغة "1 : X" تلقائياً بعد تحويل الوحدات إلى سنتيمترات.

## ✅ الميزات
- واجهة رسومية خفيفة وسهلة الاستخدام.
- تدعم وحدات الطول: سنتيمتر (cm)، متر (m)، كيلومتر (km).
- تتعامل مع إدخالات غير صحيحة وتظهر رسائل توضيحية.
- تعرض النتيجة بشكل منسق مع فواصل للقراءة السهلة.

## ⚠️ ملاحظة مهمة حول الهكتار
وحدة "hectare" مدرجة في واجهة المستخدم لكن الهكتار ليس وحدة طول خطية، بل مساحة، لذا لا يمكن حساب مقياس طول مباشر بها. عند اختيار الهكتار ستظهر رسالة أن الحساب غير ممكن.

## المتطلبات
- Python 3.8 أو أحدث
- مكتبة customtkinter

لتثبيت المتطلبات:

```powershell
python -m pip install --upgrade pip
pip install customtkinter
```

## كيف تشغّل الأداة (Windows PowerShell)
1. افتح نافذة PowerShell في مجلد المشروع.
2. شغّل الملف التالي (الملف يحتوي الكود المصدري):

```powershell
python .\مقاييس الرسم.py
# أو
py -3 .\مقاييس الرسم.py
```

3. ستظهر نافذة "Map Scale Calculator"، أدخل طول المقياس على الخريطة (بـ cm)، ثم الطول الحقيقي واختر الوحدة، ثم اضغط "Calculate Scale".

## أمثلة سريعة
- إذا كان طول الخط على الخريطة = 2 cm، والطول الحقيقي = 1 km
  - 1 km = 100000 cm → المقياس = 100000 / 2 = 1 : 50,000

## التعامل مع المدخلات
- القيم يجب أن تكون موجبة.
- عند إدخال نص غير رقمي سيظهر تحذير بطلب أرقام صحيحة.

## اقتراحات لتحسين مستقبلية
- إضافة دعم لاختيار وحدات الإدخال للمقياس على الخريطة (مثلاً mm, in).
- إضافة وظيفة لحفظ النتائج كصورة أو طباعة.
- إضافة توضيح مرئي (شريط مقياس) للمقياس الناتج.

## الترخيص
هذا المشروع بسيط ومجاني للاستخدام والتعديل. يمكنك إضافة ترخيص رسمي (مثل MIT) إذا رغبت.

## المؤلف
الصانع: Razi Ramzi ✍️

لمزيد من الاستفسارات أو اقتراحات التحسين تواصل عبر القنوات التي تفضلها.
