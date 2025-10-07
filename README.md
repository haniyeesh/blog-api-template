<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django Blog Project - README</title>
    <style>
        body { font-family: Tahoma, sans-serif; line-height: 1.6; padding: 20px; background-color: #f9f9f9; }
        h1, h2, h3 { color: #333; }
        code { background-color: #eee; padding: 2px 4px; border-radius: 4px; }
        pre { background-color: #eee; padding: 10px; border-radius: 5px; overflow-x: auto; }
        ul { margin-bottom: 15px; }
        li { margin-bottom: 8px; }
        .section { margin-bottom: 30px; }
    </style>
</head>
<body>

    <h1>Django Blog Project</h1>

    <p>این پروژه یک <strong>سیستم بلاگ</strong> است که با فریمورک <strong>Django</strong> توسعه داده شده و دارای امکانات هم برای <strong>تمپلیت سمت کاربر</strong> و هم <strong>API</strong> می‌باشد. این پروژه شامل مدیریت کاربران، پست‌ها، کامنت‌ها و لایک‌ها است.</p>

    <div class="section">
        <h2>ویژگی‌ها</h2>

        <h3>امکانات اصلی</h3>
        <ul>
            <li><strong>ثبت نام و ورود کاربران:</strong> کاربران باید برای کامنت گذاشتن، لایک کردن و ریپلای کردن وارد حساب کاربری شوند.</li>
            <li><strong>پست‌ها:</strong>
                <ul>
                    <li>نمایش لیست پست‌ها در تمپلیت و API</li>
                    <li>هر پست قابلیت لایک شدن توسط کاربران لاگین شده را دارد</li>
                </ul>
            </li>
            <li><strong>کامنت‌ها و ریپلای‌ها:</strong>
                <ul>
                    <li>کاربران می‌توانند کامنت بگذارند و به کامنت‌ها ریپلای کنند</li>
                    <li>ساختار کامنت‌ها به صورت <strong>درختی (Nested)</strong> است</li>
                    <li>تنها نویسنده یک کامنت می‌تواند آن را <strong>ویرایش یا حذف</strong> کند</li>
                    <li>کامنت‌ها قبل از نمایش نیاز به تایید <strong>سوپریوزر</strong> دارند</li>
                    <li>API مجزا برای دریافت، ایجاد و مدیریت کامنت‌ها و ریپلای‌ها موجود است</li>
                </ul>
            </li>
            <li><strong>صفحه‌بندی (Pagination):</strong> هم در تمپلیت و هم در API برای لیست پست‌ها و کامنت‌ها پیاده‌سازی شده است</li>
        </ul>

        <h3>دسترسی‌ها و مجوزها</h3>
        <ul>
            <li>فقط کاربران لاگین شده می‌توانند لایک کنند و کامنت بگذارند</li>
            <li>سوپریوزرها مسئول <strong>تایید و انتشار کامنت‌ها</strong> هستند</li>
            <li>نویسنده هر کامنت قادر به <strong>ویرایش و حذف</strong> کامنت خودش است</li>
        </ul>

        <h3>API</h3>
        <ul>
            <li>نمایش بلاگ‌ها و کامنت‌ها از طریق API</li>
            <li>API کامنت‌ها و ریپلای‌ها دارای ساختار درختی و پشتیبانی از عملیات CRUD برای نویسنده‌ها</li>
        </ul>
    </div>

 

</body>
</html>
