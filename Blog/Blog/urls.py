from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from posting import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Authentication
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

    # Home
    path('', views.index, name='index'),

    # Include additional posting routes
    path('', include('posting.urls')),

    # Profile
    path('profile/update/', views.update_profile, name='update_profile'),

    # User Management
    path('users/', views.manage_users, name='manage_users'),
    path('users/add/', views.add_user, name='add_user'),
    path('users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('users/deactivate/<int:user_id>/', views.deactivate_user, name='deactivate_user'),

    # Transaction Management
    path('transactions/', views.manage_transactions, name='manage_transactions'),
    path('transactions/add/', views.add_transaction, name='add_transaction'),
    path('transactions/edit/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),
    path('transactions/delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    path('transactions/export/', views.export_transactions_csv, name='export_transactions_csv'),
    path('export-transactions/', views.export_transactions_csv, name='export_transactions_csv'),
    path('transaction-history/', views.transaction_history, name='transaction_history'),

    # Points & Rewards
    path('redeem-points/', views.redeem_points, name='redeem_points'),
    path('redemption-history/', views.redemption_history, name='redemption_history'),
    path('check-balance/', views.check_balance, name='check_balance'),
    path('point-redemption/', views.point_redemption_management, name='point_redemption_management'),
    path('point-redemption-management/', views.point_redemption_management, name='point_redemption_management'),
    path('get-updated-balance/', views.get_updated_balance, name='get_updated_balance'),

    # Dashboard
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Bank and Nasabah
    path('detail_bank/<int:id>/', views.detail_bank, name='detail_bank'),
    path('daftar-nasabah/<int:bank_id>/', views.daftar_nasabah, name='daftar_nasabah'),

    # Informasi & Slider
    path('kelola-informasi/', views.kelola_slider, name='kelola_informasi'),
    path('hapus-slide/<int:id>/', views.hapus_slide, name='hapus_slide'),

    # Mitra Management
    path('kelola-mitra/', views.kelola_mitra, name='kelola_mitra'),
    path('edit-mitra/<int:pk>/', views.edit_mitra, name='edit_mitra'),
    path('delete-mitra/<int:pk>/', views.delete_mitra, name='delete_mitra'),

    # Link Management
    path('admin-yayasan/tambah-link/', views.kelola_link, name='kelola_link'),
    path('admin-yayasan/kelola-link/hapus/<int:link_id>/', views.hapus_link, name='hapus_link'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
