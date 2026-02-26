import datetime

mock_input_data = [
    {"json": {"patientId": "P-101", 
              "test": "potassium", 
              "value": 5.8, 
              "unit": "mmol/L", 
              "collectedAt": "2024-05-20"}},
    {"json": {"patientId": "P-102", 
              "test": "glucose", 
              "value": 5.0, 
              "unit": "mmol/L", 
              "collectedAt": "2024-05-20"}}
]

def process_medical_data(items):
    result = []
    
    thresholds = {
        "potassium": {"min": 3.5, "max": 5.0},
        "glucose": {"min": 3.9, "max": 6.9}
    }
    
    for item in items:
        data = item.get("json", {})
        
        patient_id = data.get("patientId")
        test_val = data.get("test")
        value = data.get("value")
        unit = data.get("unit")
        collected_at = data.get("collectedAt")
        
        if not patient_id or not test_val or value is None or not unit or not collected_at:
            raise ValueError("Missing mandatory fields")
            
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a numeric type")
            
        test_name = str(test_val).lower()
        limits = thresholds.get(test_name)
        
        if limits and (value < limits["min"] or value > limits["max"]):
            is_critical = True
            severity = "critical"
            triage_reason = f"Value {value} is outside normal range."
            recommended_action = "срочное уведомление врача"
        else:
            is_critical = False
            severity = "normal"
            triage_reason = "Value is normal or no thresholds defined."
            recommended_action = "обработка"
            
        new_data = {
            "ok": True,
            "isCritical": is_critical,
            "patientId": patient_id,
            "test": test_name,
            "value": value,
            "unit": unit,
            "severity": severity,
            "triageReason": triage_reason,
            "recommendedAction": recommended_action,
            "receivedAt": datetime.datetime.now(datetime.UTC).isoformat().replace("+00:00", "Z")
        }
        
        result.append({"json": new_data})
        
    return result

processed_data = process_medical_data(mock_input_data)

for record in processed_data:
    print(record)