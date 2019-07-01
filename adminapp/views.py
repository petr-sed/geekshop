from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView

class IsSuperUserView(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

"""User"""

class UsersListView(IsSuperUserView, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        context['title'] = 'Пользователи, Админка'
        return context

class UserCreateView(IsSuperUserView, CreateView):
    model = ShopUser
    template_name = 'adminapp/user_create.html'
    success_url = reverse_lazy('admin_custom:users')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание пользователя, Админка'
        return context

class UserUpdateView(IsSuperUserView, UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_create.html'
    success_url = reverse_lazy('admin_custom:users')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        title = ShopUser.objects.get(pk=self.kwargs.get('pk')).username
        context['title'] = '{}, Админка'.format(title)
        return context

class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('admin_custom:users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserDeleteView, self).get_context_data(**kwargs)
        title = ShopUser.objects.get(pk=self.kwargs.get('pk')).username
        context['title'] = 'Удаление {}'.format(title)
        return context

"""Category"""

class CategoryListView(IsSuperUserView, ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Категории, Админка'
        return context

class CategoryCreateView(IsSuperUserView, CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_create.html'
    success_url = reverse_lazy('admin_custom:categories')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание категории, Админка'
        return context


class CategoryUpdateView(IsSuperUserView, UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_create.html'
    success_url = reverse_lazy('admin_custom:categories')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        title = ProductCategory.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = '{}, Админка'.format(title)
        return context

class CategoryDeleteView(IsSuperUserView, DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin_custom:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryDeleteView, self).get_context_data(**kwargs)
        title = ProductCategory.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = 'Удаление {}'.format(title)
        return context

"""Products"""

class ProductListView(IsSuperUserView, ListView):
    model = Product
    template_name = 'adminapp/products.html'

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        if self.kwargs.get('category_pk'):
            queryset = queryset.filter(category=self.kwargs.get('category_pk'))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Все продукты, Админка'
        context['categories'] = ProductCategory.objects.all()
        return context

class ProductDetailView(IsSuperUserView, DetailView):
    model = Product
    template_name = 'adminapp/product.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        title = Product.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = '{}, Админка'.format(title)
        return context

class ProductCreateView(IsSuperUserView, CreateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin_custom:products')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание продукта, Админка'
        return context


class ProductUpdateView(IsSuperUserView, UpdateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin_custom:products')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        title = Product.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = '{}, Админка'.format(title)
        return context


class ProductDeleteView(IsSuperUserView, DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('admin_custom:products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDeleteView, self).get_context_data(**kwargs)
        title = Product.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = 'Удаление {}'.format(title)
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
