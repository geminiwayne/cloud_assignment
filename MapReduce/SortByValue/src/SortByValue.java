/*
* Team 4
* Melbourne, Sydney, Brisbane, Perth
* Danping Zeng      777691
* Dong Wang         773504
* Jia Zhen          732355
* Jinghan Liang     732329
* Sixue Yang        722804
* 
* This is a tool used to sort json objects by their values
*/

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class SortByValue {
	@SuppressWarnings({ "unchecked" })
	public static void main(String[] args) {
		String[] FileName = args;
		
		JSONParser parser = new JSONParser();
		
		Map<String, Integer> unsorted = new HashMap<String, Integer>();
		Map<String, Integer> sorted = new LinkedHashMap<String, Integer>();
		try {
			JSONObject file = (JSONObject) parser.parse(new FileReader(FileName[0]));
			JSONArray jsons = (JSONArray) file.get("rows");
			for(Object o: jsons){
				JSONObject json = (JSONObject) o;
				unsorted.put((String)json.get("key"), ((Long)json.get("value")).intValue());
			}
			
			// Convert Map to List of Map
	        List<Map.Entry<String, Integer>> list = new LinkedList<Map.Entry<String, Integer>>(unsorted.entrySet());

	        // Sort list with Collections.sort(), provide a custom Comparator
	        // Try switch the o1 o2 position for a different order
	        Collections.sort(list, new Comparator<Map.Entry<String, Integer>>() {
	            public int compare(Map.Entry<String, Integer> o1,
	                               Map.Entry<String, Integer> o2) {
	                return (o2.getValue()).compareTo(o1.getValue());
	            }
	        });
	        
	        // Loop the sorted list and put it into a new insertion order Map LinkedHashMap
	        for (Map.Entry<String, Integer> entry : list) {
	            sorted.put(entry.getKey(), entry.getValue());
	        }
	        
	        // Convert map into JSONArray
	        JSONArray NewJsons = new JSONArray();
	        for (String key : sorted.keySet()) {
	            JSONObject NewJson = new JSONObject();
	            NewJson.put(key, sorted.get(key));
	            NewJsons.add(NewJson);
	        }

	        // Write new json file
	        JSONObject obj = new JSONObject();
	        obj.put("rows", NewJsons);
	        try (FileWriter writer = new FileWriter(FileName[0])) {
	            writer.write(obj.toJSONString());
	            writer.flush();
	        } catch (IOException e) {
	            e.printStackTrace();
	        }
	        
		} catch(FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ParseException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	
}
