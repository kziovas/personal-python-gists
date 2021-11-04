import numpy as np
import pandas as pd
import xarray as xr

da = xr.DataArray(
    np.random.random(size=(2, 12)),
    dims=("year", "month"),
    coords={"month": np.linspace(1, 12, num=12).astype(int), "year": [2000, 2001]},
)

print(da)


rolling_mean = da.stack(z=("year", "month")).rolling(z=3).mean()

print(rolling_mean)
