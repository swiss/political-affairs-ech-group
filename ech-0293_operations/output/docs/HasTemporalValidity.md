

## Class: HasTemporalValidity 


_A mixin class that provides slots for modeling a temporal validity of information (not of an event)._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| valid_from | 0..1 <br/> [Date](Date.md) | The date from which the information is valid.  |
| valid_through | 0..1 <br/> [Date](Date.md) | The date until which the information is valid, inclusive.  |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available.  |



### Mixin Usage

| mixed into | description |
| --- | --- |





















</div>