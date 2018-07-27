from haystack import indexes
from .models import Timeframes,Drawers,Cards
    
class TimeFramesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    timeframe = indexes.CharField(model_attr='timeframe')  # Field name made lowercase.
    timeframedescription = indexes.CharField(model_attr='timeframedescription')  # Field name made lowercase.
    
    def get_model(self):
        return Timeframes
    
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.order_by('-timeframe')
    
class DrawersIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    drawerid = indexes.CharField(model_attr='drawerid')  # Field name made lowercase.
    drawerpath = indexes.CharField(model_attr='drawerpath')  # Field name made lowercase.
    drawerdescription = indexes.CharField(model_attr='drawerdescription')  # Field name made lowercase.
    drawerdescription_ngram = indexes.NgramField(model_attr='drawerdescription')  # Field name made lowercase.
    drawerdescription_edgegram = indexes.EdgeNgramField(model_attr='drawerdescription')  # Field name made lowercase.
    timeframe = indexes.CharField(model_attr='timeframe')  # Field name made lowercase.

    def get_model(self):
        return Drawers
    
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.order_by('-drawerid')
        
class CardsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    cardid = indexes.CharField(model_attr='cardid')  # Field name made lowercase.
    drawerid = indexes.CharField(model_attr='drawerid', faceted=True)  # Field name made lowercase.
    timeframe = indexes.CharField(model_attr='timeframe', null=True)  # Field name made lowercase.
    cardtext = indexes.CharField(model_attr='cardtext')  # Field name made lowercase.
    cardnumber = indexes.CharField(model_attr='cardnumber')  # Field name made lowercase.
    cardgroup = indexes.CharField(model_attr='cardgroup', null=True)  # Field name made lowercase.


    def get_model(self):
        return Cards
    
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.order_by('-cardid')
