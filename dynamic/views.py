import os
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

def index(request):
  return render(request, 'dynamic/index.html')

def show_date(request):
    # สร้างวันที่และเวลาปัจจุบัน
    current_datetime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    # ใช้ render แทน HttpResponse เพื่อแสดง template date.html
    return render(request, 'dynamic/date.html', {'current_datetime': current_datetime})

def show_directoryListing(request):
    # รับค่า directory_path จาก GET parameter
    directory_path = request.GET.get('directory_path', '/')  # กำหนด default directory path

    # ถ้าคลิกเข้าไปที่ไฟล์
    file_path = request.GET.get('file_path', None)
    
    if file_path:
        try:
            # เปิดไฟล์และส่งเนื้อหากลับ
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    file_content = file.read()
                return HttpResponse(f"<h1>File Content</h1><pre>{file_content}</pre>")
            else:
                return HttpResponse(f"File {file_path} not found.", status=404)
        except Exception as e:
            return HttpResponse(f"Error reading file: {str(e)}", status=500)

    # หากไม่คลิกเข้าไปที่ไฟล์ ให้แสดงรายการไฟล์ใน directory
    try:
        # ตรวจสอบว่า path นี้มีอยู่จริงหรือไม่
        if not os.path.exists(directory_path):
            return HttpResponse(f"Directory {directory_path} not found.", status=404)

        # ใช้ os.listdir() เพื่อดึงรายการไฟล์จากไดเรกทอรี
        files = os.listdir(directory_path)
        
        # สร้างเนื้อหาสำหรับแสดงใน response
        directory_content = "<h1>Directory Listing</h1>"  # เพิ่มคำว่า "Directory Listing"
        
        if files:
            directory_content += "<ul>"
            for file in files:
                file_path = os.path.join(directory_path, file)

                # ถ้าเป็น directory, ลิงก์ไปที่ directory
                if os.path.isdir(file_path):
                    directory_content += f'<li><a href="/dynamic/directory/?directory_path={file_path}">{file}/</a></li>'
                else:
                    # ถ้าเป็นไฟล์, ให้คลิกเพื่อดูเนื้อหาของไฟล์
                    directory_content += f'<li><a href="/dynamic/directory/?file_path={file_path}">{file}</a></li>'
            directory_content += "</ul>"
        else:
            directory_content += "<p>No files found in the directory.</p>"

        # ใช้ render แทน HttpResponse เพื่อแสดง template showdirectory.html
        return render(request, 'dynamic/showdirectory.html', {'directory_content': directory_content})

    except FileNotFoundError:
        # กรณีไม่พบไดเรกทอรี
        return HttpResponse(f"Directory {directory_path} not found.", status=404)
