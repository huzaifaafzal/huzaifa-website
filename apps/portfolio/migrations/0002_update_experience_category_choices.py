from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experience",
            name="category",
            field=models.CharField(
                choices=[
                    ("cloud", "Cloud / DevOps"),
                    ("journalism", "Writing / Journalism"),
                    ("ai_research", "AI Research / Academic"),
                    ("security", "Cybersecurity"),
                ],
                default="cloud",
                max_length=30,
            ),
        ),
    ]
