# 0x04. Pagination

## Learning Objectives
* How to paginate a dataset with simple page and page_size parameters
* How to paginate a dataset with hypermedia metadata
* How to paginate in a deletion-resilient manner

## Pagination
* Most endpoints that returns a list of entities will need to have some sort of pagination.

* Without pagination, a simple search could return millions or even billions of hits causing extraneous network traffic.

* Paging requires an implied ordering. By default this may be the item’s unique identifier, but can be other ordered fields such as a created date.

## Offset Pagination

* This is the simplest form of paging. Limit/Offset became popular with apps using SQL databases which already have LIMIT and OFFSET as part of the SQL SELECT Syntax. Very little business logic is required to implement Limit/Offset paging.

* Limit/Offset Paging would look like GET /items?limit=20&offset=100. This query would return the 20 rows starting with the 100th row.

## Keyset Pagination

* Keyset pagination uses the filter values of the last page to fetch the next set of items. Those columns would be indexed.

* Keyset pagination can work very well for data with a single natural high cardinality key such as time series or log data which can use a timestamp.

## Seek Pagination

* Seek Paging is an extension of Keyset paging. By adding an after_id or start_id URL parameter, we can remove the tight coupling of paging to filters and sorting. Since unique identifiers are naturally high cardinality, we won’t run into issues unlike if sorting by a low cardinality field like state enums or category name.

## HATEOAS

* Stands for: Hypermedia As The Engine Of The Application State.
* Hypermedia are links to different parts of the API, like <a> tag in web pages.
* HATEOAS makes APIs self-descriptive / self-discovarable.
* HATEOS allow the API to evolve independently of the consuming applications without breaking.
* It is a component of the REST application architecture that distinguishes it from other network application architectures.
* What actions are possible varies as the state of the resource varies.
