Changelog
=========

0.2.16 (unreleased)
-------------------

- Nothing changed yet.


0.2.15 (2017-02-08)
-------------------

- Set good class for listingcards.pt
  [mgennart]


0.2.14 (2016-09-28)
-------------------

- Fix geomap import from collective.geo.leaflet.
  [bsuttor]


0.2.13 (2016-04-27)
-------------------

- Fix typo import step registry.


0.2.12 (2016-04-27)
-------------------

- Add upgrade step for export view (to csv file).


0.2.11 (2016-04-18)
-------------------

- Add a new view "collective_directory_export_view" on directory to export cards to csv file.


0.2.10 (2016-01-15)
-------------------

- remove special chars in str replacement
- reindex cards in collective_directory_assign_geolocation view


0.2.9 (2016-01-13)
------------------

- Add new method that clean a string. Use it to change category_name to category_id when importing cards from csv.


0.2.8 (2016-01-13)
------------------

- Remove service OpenMapQuest.


0.2.7 (2016-01-08)
------------------

- Add translation for all content types.
  [bsuttor]


0.2.6 (2016-01-08)
------------------

- Bad release.


0.2.5 (2016-01-08)
------------------

- Add new view to set Geolocation to each Cards in a directory.
  [boulch]

- Change zip_code schema from int to string.
  [boulch]

0.2.4 (2015-07-07)
------------------

- Correct a css class for email in detailcard.pt

- Fix card in card are now return into json view.
  [bsuttor]

- Open website link into a new page.
  [bsuttor]


0.2.3 (2015-02-10)
------------------

- Fix js error, use maxHeight instead of maxheight
  [bsuttor]


0.2.2 (2015-02-03)
------------------

- Use maxheight instead of height in control directory.
  [bsuttor]


0.2.1 (2015-02-03)
------------------

- Sort category by id in legend.
  [bsuttor]

- Fix height and overflow for category legend
  [bsuttor]


0.2.0 (2015-02-02)
------------------

- Do not use geojson for directory view. Use marker and layerGroup instead
  [bsuttor]


0.1.8 (2015-01-20)
------------------

- Check if portal_directory exists.


0.1.7 (2015-01-15)
------------------

- Try to add markercluster (Leaflet), first step.
  [bsuttor]


0.1.6 (2015-01-15)
------------------

- Order map and force width to 100% on install.
  [bsuttor]

- Fix: card not imported into zcml.
  [bsuttor]


0.1.5 (2015-01-14)
------------------

- Imporve upgrade step with class change.
  [bsuttor]


0.1.4 (2015-01-14)
------------------

- Add import from csv tab for a directory.
  [bsuttor]

- Improve creation of geojson leaflet objects.
  [bsuttor]


0.1.3 (2014-12-05)
------------------

- Update migration category. If a card has multi category,
  it choose first one and forgot others.
  [bsuttor]


0.1.2 (2014-12-04)
------------------

- Add migration profile.
  [bsuttor]

- Add migrate schedule opening_hours
  [schminitz]


0.1.1 (2014-10-07)
------------------

- Add upgrade step to rename all object with name from title.
  [bsuttor]

- Fix tests
  [laulaz]


0.1 (2014-08-21)
----------------

- Initial release
