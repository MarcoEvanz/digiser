from django.db import models

# Create your models here.
from django.db import models
from django.db.models.functions import Now
from django.contrib.auth.models import User
from .field_option import Options
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator,RegexValidator,MinValueValidator

class Project(models.Model):
    project_name = models.CharField(max_length =20,default= '', verbose_name="Tên dự án", blank = True)
    sub_project_name = models.CharField(max_length =20, default= '', verbose_name="Tên dự án con", blank = True)
    project_description = models.CharField(max_length =100, default= '',  verbose_name="Mô tả dự án", blank = True) 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, null=True, blank=True, on_delete= models.SET_NULL)
    is_active = models.BooleanField(default=True)
    description = models.CharField(max_length=200)



class Document(models.Model):
    user = models.ForeignKey(User, verbose_name="Người tạo", blank=True, null=True, on_delete= models.SET_NULL)
    project = models.ForeignKey(Project,verbose_name="Dự án",null=True, blank=True, on_delete= models.SET_NULL)
    document_name = models.CharField(max_length =100, default= '', verbose_name="Tên tài liệu", blank = True)
    document_url = models.CharField(max_length =100, default= '', verbose_name="Đường dẫn tài liệu", blank = True)
    insert_status = models.CharField(max_length =10, default= 'new', verbose_name="Trạng thái nhập", blank = True)
    check_status = models.CharField(max_length =10, default= 'new', verbose_name="Trạng thái kiểm tra", blank = True)
    created_at = models.DateTimeField(verbose_name="Ngày tạo", db_default=Now())
    def __str__(self):
        return self.document_name


class Marriage_Certificate_Document(models.Model):
    so = models.CharField(max_length =10, default= 'null', verbose_name = 'Số', blank = True)
    trangSo= models.CharField(max_length =10, default= '', verbose_name = 'Trang Số', blank = True)
    ngayDangKy = models.DateField( default= '', verbose_name = 'Ngày Đăng Ký', blank = True)
    loaiDangKy = models.IntegerField(choices= Options.REGISTER_STATUS, default = '1', verbose_name='Loại Đăng Ký', blank = True)
    nguoiKy = models.CharField(max_length=100, default=' ', verbose_name='Người Ký', blank=True)
    chucVuNguoiKy = models.CharField(max_length=100, default='Công Chức Tư Pháp - Hộ Tịch', verbose_name='Chức vụ người ký', blank=True)
    nguoiThucHien = models.CharField(max_length=100, default='', verbose_name='Người thực hiện', blank=True)
    #ghiChu = models.CharField(max_length=500, default=' ', verbose_name='Ghi chú', blank=True,validators=[RegexValidator(regex='^[a-zA-Z0-9_]*$',message='Không được chứa ký tự đặc biệt')])
    tinhTrangKetHon = models.IntegerField(choices= Options.MARRIED_STATUS, default = '4', verbose_name='Tình trạng kết hôn', blank=True)
    
    chongHoTen = models.CharField(max_length=100, default=' ', verbose_name='Chồng_Họ tên', blank=True)
    chongNgaySinh = models.DateField( default=' ', verbose_name='Chồng_Ngày sinh', blank=True)
    chongDanToc = models.CharField(max_length=30, choices= Options.DANTOC_LIST, default= '', verbose_name='Chồng_Dân tộc', blank=True)
    chongQuocTich = models.CharField(max_length=100, choices= Options.COUNTRIES_LIST, default= '', verbose_name='Chồng_Quốc tịch', blank=True)
    chongLoaiCuTru = models.IntegerField(choices= Options.RESIDENCE_TYPE, verbose_name='Chồng_Loại cư trú', blank=True)
    #chongNoiCuTru = models.CharField(max_length=100, default=' ', verbose_name='Chồng_Nơi cư trú', blank=True)
    chongLoaiGiayToTuyThan = models.IntegerField(choices= Options.DENTIFICATION_TYPE, default= '', verbose_name='Chồng_Loại giấy tờ tùy thân', blank=True)
    chongSoGiayToTuyThan = models.CharField(max_length=50, default=' ', verbose_name='Chồng_Số giấy tờ tùy thân', blank=True)
    chongNgayCapGiayToTuyThan = models.DateField( default=' ', verbose_name='Chồng_Ngày cấp giấy tờ tùy thân', blank=True)
    #chongNoiCapGiayToTuyThan = models.CharField(max_length=500, default=' ', verbose_name='Chồng_Nơi cấp giấy tờ tùy thân', blank=True)

    voHoTen = models.CharField(max_length=100, default=' ', verbose_name='Vợ_Họ tên', blank=True)
    voNgaySinh = models.DateField( default=' ', verbose_name='Vợ_Ngày sinh', blank=True)
    voDanToc = models.CharField(max_length=100, choices= Options.DANTOC_LIST, default= '', verbose_name='Vợ_Dân tộc', blank=True)
    voQuocTich = models.CharField(max_length=100, choices= Options.COUNTRIES_LIST, default= '', verbose_name='Vợ_Quốc tịch', blank=True)
    voQuocTichKhac = models.CharField(max_length=100, choices= Options.COUNTRIES_LIST, default= '', verbose_name='Vợ_Quốc tịch khác', blank=True)
    voLoaiCuTru = models.IntegerField(choices= Options.RESIDENCE_TYPE, verbose_name='Vợ_Loại cư trú', blank=True)
    #voNoiCuTru = models.CharField(max_length=500, default=' ', verbose_name='Vợ_Nơi cư trú', blank=True)
    voLoaiGiayToTuyThan = models.IntegerField(choices= Options.DENTIFICATION_TYPE, default= '', verbose_name='Vợ_Loại giấy tờ tùy thân', blank=True)
    voSoGiayToTuyThan = models.CharField(max_length=50, default=' ', verbose_name='Vợ_Số giấy tờ tùy thân', blank=True)
    voNgayCapGiayToTuyThan = models.DateField( default=' ', verbose_name='Vợ_Ngày cấp giấy tờ tùy thân', blank=True)
    #voNoiCapGiayToTuyThan = models.CharField(max_length=500, default=' ', verbose_name='Vợ_Nơi cấp giấy tờ tùy thân', blank=True)




    def __str__(self):
        # return self.document.document_name
        return str(self.pk)