from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Course, Exam, Material, Fee
from .forms import ContactForm

# Home Page View
def home_view(request):
    courses = Course.objects.all()
    exams = Exam.objects.all()
    materials = Material.objects.all()
    fees = Fee.objects.all()

    context = {
        'courses': courses,
        'exams': exams,
        'materials': materials,
        'fees': fees
    }
    return render(request, 'college/index.html', context)

# Contact Page View
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save form data to the database
            form.save()

            # Extract cleaned data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Prepare email content
            subject = f"New Contact Us Message from {name}"
            body = f"From: {name} <{email}>\n\nMessage:\n{message}"
            from_email = 'your-email@gmail.com'  # Replace with your email
            to_email = ['your-email@gmail.com']  # Replace with your recipient email(s)

            try:
                send_mail(subject, body, from_email, to_email, fail_silently=False)
                messages.success(request, "✅ Your message has been sent successfully!")
            except Exception as e:
                messages.error(request, f"❌ Failed to send message: {e}")

            return redirect('contact')  # Redirect back to the contact page
    else:
        form = ContactForm()

    return render(request, 'college/contact.html', {'form': form})
