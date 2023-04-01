# Generated by Django 4.1.7 on 2023-04-01 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0005_alter_match_team_a_goal_alter_match_team_b_goal"),
    ]

    operations = [
        migrations.CreateModel(
            name="Action",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("minutes", models.IntegerField()),
                (
                    "action",
                    models.CharField(
                        choices=[
                            ("goal", "Goal"),
                            ("assist", "Assist"),
                            ("yellow card", "Yellow Card"),
                            ("red card", "Red Card"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="app.match"
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="app.player"
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="app.team"
                    ),
                ),
            ],
        ),
    ]
