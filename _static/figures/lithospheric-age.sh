#!/usr/bin/env bash
gmt begin
	gmt figure lithospheric-age PNG A,E100,Qt4,Qg2
	# Get gradients of the relief from N45E
	gmt grdgradient @earth_relief_20m -Nt1.25 -A45 -Gintens.nc
	gmt basemap -JR220/20c -R@earth_age_20m -Bf
	gmt makecpt -Cinferno -T0/280/10 -Ic --COLOR_NAN=grey83
	# Plot age grid first using age cpt
	gmt grdimage @earth_age_20m -Iintens.nc
	gmt colorbar -DJBC+w10c+o0/0.5c -B50 -Bx+l"Lithospheric Age [Ma]"
	# Extract a topography CPT
	gmt makecpt -Cdem2 -T0/6000
	# Clip to expose land areas only
	gmt coast -Gc
	# Overlay relief over land only using dem cpt
	gmt grdimage @earth_relief_05m -I+a45+nt1.25
	# Undo clipping and overlay gridlines
	gmt coast -Q
	rm intens.nc
gmt end show
