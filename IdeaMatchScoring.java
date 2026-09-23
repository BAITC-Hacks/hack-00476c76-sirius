import java.util.*;

public class IdeaMatchScoring {
    private static final LinkedHashMap<String,Integer> WEIGHTS = new LinkedHashMap<>();
    static {
        WEIGHTS.put("context",20); WEIGHTS.put("data",20); WEIGHTS.put("expected",15);
        WEIGHTS.put("success",15); WEIGHTS.put("constraints",10); WEIGHTS.put("users",10); WEIGHTS.put("contact",10);
    }
    public static int readiness(Map<String,String> card){
        int score=0;
        for(var e:WEIGHTS.entrySet()){
            String value=card.getOrDefault(e.getKey(), "").trim();
            if(!value.isEmpty()) score += e.getValue();
        }
        return score;
    }
    public static String level(int score){
        if(score<40) return "Draft"; if(score<70) return "Working"; if(score<90) return "Ready"; return "Priority";
    }
}
