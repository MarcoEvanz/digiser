from django import forms
from .field_option import Options
from .models import Project,Marriage_Certificate_Document, Profile,User
import re
from django.utils import timezone


def checkUpper(statement):
    upper= str(statement)
    for word in upper.split():
        if not word[0].isupper() or re.search(r'\d', word):
            raise ValueError("Each word must start with an uppercase letter and should not include numbers.")
    return statement
def checkMinMax(statement,min,max):
    if (statement < min):
        raise forms.ValidationError(f"vaule has to larger than {min}")
    if (statement > max):
        raise forms.ValidationError(f"vaule has to less than {max}")
def checkLength(statement):
    length= len(statement)
    if(length != 9 or length != 0):
        raise forms.ValidationError("length has to be 9 or full")
    if len(statement) == 9 and re.search('[a-zA-Z]', statement):
        raise forms.ValidationError("should not include characters")

class Marriage_Certificate_Form(forms.ModelForm):
    class Meta:
        model = Marriage_Certificate_Document
        fields = '__all__'
    so = forms.CharField(max_length =10, label='Số')
    trangSo= forms.IntegerField(label='Trang Số' )
    ngayDangKy = forms.DateField(label='Ngày Đăng Ký')
    loaiDangKy = forms.IntegerField(widget=forms.Select(choices= Options.REGISTER_STATUS),label='Loại Đăng Ký')
    nguoiKy = forms.CharField(max_length=100, label='Người Ký')
    chucVuNguoiKy = forms.CharField(max_length=100,label='Chức Vụ Người Ký')
    nguoiThucHien = forms.CharField(max_length=100,label='Người Thực Hiện')
    tinhTrangKetHon = forms.IntegerField(widget=forms.Select(choices= Options.MARRIED_STATUS),label='Tình Trạng Kết hôn')

    chongHoTen = forms.CharField(max_length=100, label='Chồng_Họ tên')
    chongNgaySinh = forms.DateField(label='Chồng_Ngày sinh')
    chongDanToc = forms.CharField(widget=forms.Select(choices= Options.DANTOC_LIST),label='Chồng_Dân tộc')
    chongQuocTich = forms.CharField(widget=forms.Select(choices= Options.COUNTRIES_LIST),label='Chồng_Quốc Tịch')
    chongLoaiCuTru = forms.IntegerField(widget=forms.Select(choices= Options.RESIDENCE_TYPE),label='Chồng_Loại cư trú')
    chongLoaiGiayToTuyThan = forms.IntegerField(widget=forms.Select(choices= Options.DENTIFICATION_TYPE),label='Chồng_Loại giấy tờ tùy thân')
    chongSoGiayToTuyThan = forms.CharField(max_length=50,label='Chồng_Số giấy tờ tùy thân')
    chongNgayCapGiayToTuyThan = forms.DateField(label='Chồng_Ngày cấp giấy tờ tùy thân')

    voHoTen = forms.CharField(max_length=100, label='Vợ_Họ tên')
    voNgaySinh = forms.DateField(label='Vợ_Ngày sinh')
    voDanToc = forms.CharField( widget=forms.Select(choices= Options.DANTOC_LIST),label='Vợ_Dân tộc')
    voQuocTich = forms.CharField( widget=forms.Select(choices= Options.COUNTRIES_LIST),label='Vợ_Quốc Tịch')
    voQuocTichKhac = forms.CharField(widget=forms.Select(choices= Options.COUNTRIES_LIST),label='Vợ_Quốc Tịch Khác')
    voLoaiCuTru = forms.IntegerField(widget=forms.Select(choices= Options.RESIDENCE_TYPE),label='Vợ_Loại cư trú')
    voLoaiGiayToTuyThan = forms.IntegerField(widget=forms.Select(choices= Options.DENTIFICATION_TYPE),label='Vợ_Loại giấy tờ tùy thân')
    voSoGiayToTuyThan = forms.CharField(max_length=50, label='Vợ_Số giấy tờ tùy thân')
    voNgayCapGiayToTuyThan = forms.DateField(label='Vợ_Ngày cấp giấy tờ tùy thân')

    def clean_ngayDangKy(self):
        ngayDangKy = self.cleaned_data['ngayDangKy']
        if ngayDangKy > timezone.now().date():
            raise forms.ValidationError("Ngày Đăng Ký không được lớn hơn ngày hiện tại")
        return ngayDangKy

    def clean_chongNgaySinh(self):
        chongNgaySinh = self.cleaned_data['chongNgaySinh']
        if chongNgaySinh > timezone.now().date():
            raise forms.ValidationError("Chồng_Ngày sinh không được lớn hơn ngày hiện tại")
        return chongNgaySinh

    def clean_chongNgayCapGiayToTuyThan(self):
        chongNgayCapGiayToTuyThan = self.cleaned_data['chongNgayCapGiayToTuyThan']
        if chongNgayCapGiayToTuyThan > timezone.now().date():
            raise forms.ValidationError("Chồng_Ngày cấp giấy tờ tùy thân không được lớn hơn ngày hiện tại")
        return chongNgayCapGiayToTuyThan

    def clean_voNgaySinh(self):
        voNgaySinh = self.cleaned_data['voNgaySinh']
        if voNgaySinh > timezone.now().date():
            raise forms.ValidationError("Vợ_Ngày sinh không được lớn hơn ngày hiện tại")
        return voNgaySinh

    def clean_voNgayCapGiayToTuyThan(self):
        voNgayCapGiayToTuyThan = self.cleaned_data['voNgayCapGiayToTuyThan']
        if voNgayCapGiayToTuyThan > timezone.now().date():
            raise forms.ValidationError("Vợ_Ngày cấp giấy tờ tùy thân không được lớn hơn ngày hiện tại")
        return voNgayCapGiayToTuyThan


    def clean(self):
        cleaned_data = super().clean()
        cleaned_nguoiKy = cleaned_data.get("nguoiKy")
        cleaned_chucVuNguoiKy = cleaned_data.get("chucVuNguoiKy") 
        cleaned_nguoiThuchien = cleaned_data.get("nguoiThuchien")
        cleaned_tinhTrangKetHon = cleaned_data.get("tinhTrangKetHon")
        cleaned_loaiDangKy = cleaned_data.get("loaiDangKy")
        cleaned_chongHoTen = cleaned_data.get("chongHoTen")
        cleaned_voHoTen = cleaned_data.get("voHoTen")
        cleaned_chongLoaiGiayToTuyThan = cleaned_data.get("chongLoaiGiayToTuyThan")
        cleaned_voLoaiGiayToTuyThan = cleaned_data.get("voLoaiGiayToTuyThan")
        cleaned_chongSoGiayToTuyThan = cleaned_data.get("chongSoGiayToTuyThan")
        cleaned_voSoGiayToTuyThan = cleaned_data.get("voSoGiayToTuyThan")
        cleaned_chongLoaiCuTru= cleaned_data.get("chongLoaiCuTru")
        cleaned_voLoaiCuTru = cleaned_data.get("voLoaiCuTru")
        
        checkUpper(cleaned_nguoiKy)
        checkUpper(cleaned_chucVuNguoiKy) 
        checkUpper(cleaned_nguoiThuchien)
        checkUpper(cleaned_chongHoTen)
        checkUpper(cleaned_voHoTen)
        
        checkMinMax(cleaned_tinhTrangKetHon, 1, 4)
        checkMinMax(cleaned_loaiDangKy, 1, 3) 
        checkMinMax(cleaned_chongLoaiGiayToTuyThan, 1, 9)
        checkMinMax(cleaned_voLoaiGiayToTuyThan, 1, 9)
        checkMinMax(cleaned_chongLoaiCuTru, 0, 2)
        checkMinMax(cleaned_voLoaiCuTru, 0, 2)
        
        checkLength(cleaned_chongSoGiayToTuyThan) 
        checkLength(cleaned_voSoGiayToTuyThan)
        
        return cleaned_data
    

        
class ProjectForm(forms.ModelForm):   
    class Meta:
        model = Project
        fields = "__all__"
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"