# metadata.py
"""
File containing metadata information for WW2100 model run
"""
class UnknownFileType(BaseException):
    pass

AltScenarios = ["Ref","LowClim","HighClim","FireSuppress","UrbExpand","HighPop"]

def define_model_run(name):
    import xlrd
    model_book = xlrd.open_workbook('cascade plot parameters.xls')
    if name == "first": 
        Case = str(model_book.sheet_by_index(0).col_values(0)[1])      #find the reference model type
    else:
        Case = str(name)
        
    if "Ref_Run0" in Case:
        model = 'Reference (MIROC)'
    elif "LowClim" in Case:  
        model = 'Low Climate Change (GFDL)'
    elif "FireSuppress" in Case:  
        model = 'Upland Fire Suppression'
    elif "HighClim" in Case:  
        model = 'High Climate Change (Hadley)'
    elif "UrbExpand" in Case:  
        model = "Relaxed Urban Expansion"
    elif "HighPop" in Case:  
        model = "High Population Growth"
    else:
        raise UnknownFileType()
    return model

model_run = define_model_run("first")
##print model_run
