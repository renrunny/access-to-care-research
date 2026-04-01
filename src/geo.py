"""
Geospatial analysis utilities for access-to-care research.

Functions for drive-time calculation, catchment area mapping,
isochrone generation, and geographic disparity analysis.
"""

import geopandas as gpd
import pandas as pd
import numpy as np
from shapely.geometry import Point


def geocode_zip(zip_code: str, zip_centroid_df: pd.DataFrame) -> tuple:
    """
    Look up latitude/longitude centroid for a given ZIP code.

    Parameters
    ----------
    zip_code : str
        5-digit ZIP code.
    zip_centroid_df : pd.DataFrame
        Reference table with columns: zip, latitude, longitude.

    Returns
    -------
    tuple
        (latitude, longitude) or (None, None) if not found.
    """
    match = zip_centroid_df[zip_centroid_df["zip"] == str(zip_code)]
    if match.empty:
        return (None, None)
    return (match.iloc[0]["latitude"], match.iloc[0]["longitude"])


def calculate_haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate great-circle distance between two points in miles.

    Parameters
    ----------
    lat1, lon1 : float
        Coordinates of point 1.
    lat2, lon2 : float
        Coordinates of point 2.

    Returns
    -------
    float
        Distance in miles.
    """
    R = 3959  # Earth radius in miles
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    return 2 * R * np.arcsin(np.sqrt(a))


def create_point_geodataframe(df: pd.DataFrame, lat_col: str, lon_col: str, crs: str = "EPSG:4326") -> gpd.GeoDataFrame:
    """
    Convert a DataFrame with lat/lon columns to a GeoDataFrame.
    """
    geometry = [Point(xy) for xy in zip(df[lon_col], df[lat_col])]
    return gpd.GeoDataFrame(df, geometry=geometry, crs=crs)


def assign_drive_time_zone(minutes: float) -> str:
    """
    Categorize drive time into access zones.
    """
    if pd.isna(minutes):
        return "Unknown"
    elif minutes <= 30:
        return "0-30 min"
    elif minutes <= 60:
        return "30-60 min"
    elif minutes <= 90:
        return "60-90 min"
    else:
        return "90+ min"
