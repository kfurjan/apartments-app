"""create table

Revision ID: 9e53568cac2c
Revises:
Create Date: 2021-04-10 15:03:25.343055

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func

revision = "9e53568cac2c"
down_revision = None
branch_labels = None
depends_on = None


def create_users_table() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.Text, unique=True, nullable=False, index=True),
        sa.Column("password_digest", sa.Text, nullable=False),
        sa.Column("first_name", sa.Text),
        sa.Column("last_name", sa.Text),
        sa.Column("oib", sa.Text),
        sa.Column("date_of_birth", sa.Text),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=func.now()),
        sa.Column(
            "updated_at",
            sa.DateTime,
            nullable=False,
            server_default=func.now(),
            onupdate=func.now(),
        ),
    )


def create_renters_table() -> None:
    op.create_table(
        "renters",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False, index=True
        ),
        sa.Column("address", sa.Text),
        sa.Column("city", sa.Text),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=func.now()),
        sa.Column(
            "updated_at",
            sa.DateTime,
            nullable=False,
            server_default=func.now(),
            onupdate=func.now(),
        ),
    )


def create_guests_table() -> None:
    op.create_table(
        "guests",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("documents", sa.JSON),
        sa.Column(
            "user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False, index=True
        ),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=func.now()),
        sa.Column(
            "updated_at",
            sa.DateTime,
            nullable=False,
            server_default=func.now(),
            onupdate=func.now(),
        ),
    )


def create_receipts_table() -> None:
    op.create_table(
        "receipts",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("receipt_number", sa.Text),
        sa.Column("total", sa.Numeric),
        sa.Column(
            "guest_id",
            sa.Integer,
            sa.ForeignKey("guests.id"),
            nullable=False,
            index=True,
        ),
        sa.Column(
            "renter_id",
            sa.Integer,
            sa.ForeignKey("renters.id"),
            nullable=False,
            index=True,
        ),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=func.now()),
        sa.Column(
            "updated_at",
            sa.DateTime,
            nullable=False,
            server_default=func.now(),
            onupdate=func.now(),
        ),
    )


def create_services_table() -> None:
    op.create_table(
        "services",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text),
        sa.Column("description", sa.Text),
        sa.Column("price", sa.Numeric),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=func.now()),
        sa.Column(
            "updated_at",
            sa.DateTime,
            nullable=False,
            server_default=func.now(),
            onupdate=func.now(),
        ),
    )


def create_receipt_items_table() -> None:
    op.create_table(
        "receipt_items",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "receipt_id",
            sa.Integer,
            sa.ForeignKey("receipts.id"),
            nullable=False,
            index=True,
        ),
        sa.Column(
            "service_id",
            sa.Integer,
            sa.ForeignKey("services.id"),
            nullable=False,
            index=True,
        ),
        sa.Column("quantity", sa.Integer),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=func.now()),
        sa.Column(
            "updated_at",
            sa.DateTime,
            nullable=False,
            server_default=func.now(),
            onupdate=func.now(),
        ),
    )


def create_apartments_table() -> None:
    op.create_table(
        "apartments",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.Text, nullable=False),
        sa.Column("address", sa.Text, nullable=False),
        sa.Column("city", sa.Text, nullable=False),
        sa.Column("postal_code", sa.Text, nullable=False),
        sa.Column("latitude", sa.Numeric, nullable=False),
        sa.Column("longitude", sa.Numeric, nullable=False),
        sa.Column("description", sa.Text),
        sa.Column("price_per_night", sa.Numeric, nullable=False),
        sa.Column("available", sa.Boolean),
        sa.Column("availability_start_date", sa.Date),
        sa.Column("availability_end_date", sa.Date),
        sa.Column(
            "renter_id",
            sa.Integer,
            sa.ForeignKey("renters.id"),
            nullable=False,
            index=True,
        ),
        sa.Column("images", sa.JSON),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=func.now()),
        sa.Column(
            "updated_at",
            sa.DateTime,
            nullable=False,
            server_default=func.now(),
            onupdate=func.now(),
        ),
    )


def create_apartment_details_table() -> None:
    op.create_table(
        "apartment_details",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "apartment_id",
            sa.Integer,
            sa.ForeignKey("apartments.id"),
            nullable=False,
            index=True,
        ),
        sa.Column("checkout_time", sa.Time),
        sa.Column("on_land", sa.Boolean),
        sa.Column("square_meters", sa.Numeric),
        sa.Column("number_of_rooms", sa.Integer),
        sa.Column("wifi_present", sa.Boolean),
        sa.Column("tv_present", sa.Boolean),
        sa.Column("parking_included", sa.Boolean),
        sa.Column("rating", sa.Numeric),
        sa.Column("additional_details", sa.JSON),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=func.now()),
        sa.Column(
            "updated_at",
            sa.DateTime,
            nullable=False,
            server_default=func.now(),
            onupdate=func.now(),
        ),
    )


def create_reservations_table() -> None:
    op.create_table(
        "reservations",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "guest_id",
            sa.Integer,
            sa.ForeignKey("guests.id"),
            nullable=False,
            index=True,
        ),
        sa.Column(
            "apartment_id",
            sa.Integer,
            sa.ForeignKey("apartments.id"),
            nullable=False,
            index=True,
        ),
        sa.Column("number_of_guests", sa.Integer, nullable=False),
        sa.Column("starts_at", sa.DateTime),
        sa.Column("ends_at", sa.DateTime),
        sa.Column("additional_details", sa.Text),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=func.now()),
        sa.Column(
            "updated_at",
            sa.DateTime,
            nullable=False,
            server_default=func.now(),
            onupdate=func.now(),
        ),
    )


def create_locations_table() -> None:
    op.create_table(
        "locations",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.Text, nullable=False),
        sa.Column("description", sa.Text),
        sa.Column(
            "type_id", sa.Integer, sa.ForeignKey("types.id"), nullable=False, index=True
        ),
        sa.Column("working_hours_monday", sa.Text),
        sa.Column("working_hours_tuesday", sa.Text),
        sa.Column("working_hours_wednesday", sa.Text),
        sa.Column("working_hours_thursday", sa.Text),
        sa.Column("working_hours_friday", sa.Text),
        sa.Column("working_hours_saturday", sa.Text),
        sa.Column("working_hours_sunday", sa.Text),
        sa.Column("additional_details", sa.JSON),
        sa.Column("city", sa.Text, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=func.now()),
        sa.Column(
            "updated_at",
            sa.DateTime,
            nullable=False,
            server_default=func.now(),
            onupdate=func.now(),
        ),
    )


def create_location_types_table() -> None:
    op.create_table(
        "location_types",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("type", sa.Text, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=func.now()),
        sa.Column(
            "updated_at",
            sa.DateTime,
            nullable=False,
            server_default=func.now(),
            onupdate=func.now(),
        ),
    )


def create_ratings_table() -> None:
    op.create_table(
        "ratings",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "rated_by_user_id",
            sa.Integer,
            sa.ForeignKey("users.id"),
            nullable=False,
            index=True,
        ),
        sa.Column("rating", sa.Numeric, nullable=False),
        sa.Column("comment", sa.Text),
        sa.Column("subject_id", sa.Integer, nullable=False),
        sa.Column("subject_type", sa.Text, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=func.now()),
        sa.Column(
            "updated_at",
            sa.DateTime,
            nullable=False,
            server_default=func.now(),
            onupdate=func.now(),
        ),
    )


def upgrade() -> None:
    create_users_table()
    create_renters_table()
    create_guests_table()
    create_receipts_table()
    create_services_table()
    create_receipt_items_table()
    create_apartments_table()
    create_apartment_details_table()
    create_reservations_table()
    create_locations_table()
    create_location_types_table()
    create_ratings_table()


def downgrade() -> None:
    op.drop_table("ratings")
    op.drop_table("location_types")
    op.drop_table("locations")
    op.drop_table("reservations")
    op.drop_table("apartment_details")
    op.drop_table("apartments")
    op.drop_table("receipt_items")
    op.drop_table("services")
    op.drop_table("receipts")
    op.drop_table("guests")
    op.drop_table("renters")
    op.drop_table("users")
