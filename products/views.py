from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import *
from checkout.models import *
from .forms import ProductForm


def all_products(request):
    products = Product.objects.all()
    query = request.GET.get("q")
    category = request.GET.get("category")

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    if category:
        products = products.filter(category__name__iexact=category)

    context = {"products": products, "search_term": query}

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """Eine Ansicht, um einzelne Produktdetails anzuzeigen"""
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        rating = request.POST.get("rating")
        review = request.POST.get("review")
        try:
            Review.objects.create(
                user=request.user, rating=rating, body=review, product=product
            )
        except Exception:
            messages.error(request, "You can't write a review for this product")

    context = {
        "product_id": product_id,
        "product": product,
    }

    return render(request, "products/product_detail.html", context)


@login_required
def review_feedback(request, product_id, review_id, choice):
    """Bewertung bearbeiten"""
    review = get_object_or_404(Review, id=review_id)
    if choice == 1:
        if request.user not in review.unhelpful.all():
            review.helpful.add(request.user)
    elif choice == 2:
        if request.user not in review.helpful.all():
            review.unhelpful.add(request.user)

    return redirect(reverse("product_detail", args=[product_id]))


@login_required
def delete_review(request, product_id, review_id):
    """Bewertung löschen"""
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete()
    messages.success(request, "Review deleted successfully")
    return redirect(reverse("product_detail", args=[product_id]))


@login_required
def add_product(request):
    """Ein Produkt Hinzufügen zum Shop"""
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            product.created_by = request.user
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to add product. Please ensure the form is valid."
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {"form": form}
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Ein Produkt vom Shop löschen"""
    product = get_object_or_404(Product, created_by=request.user, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))


@login_required
def edit_product(request, product_id):
    """Ein Produkt zum Shop bearbeiten"""
    product = get_object_or_404(Product, created_by=request.user, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to update product. Please ensure the form is valid."
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {"form": form, "product": product}
    return render(request, template, context)


@login_required
def my_products(request):
    products = Product.objects.filter(created_by=request.user)
    template = "products/my_products.html"
    context = {"products": products}
    return render(request, template, context)
