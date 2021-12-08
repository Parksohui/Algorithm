import java.util.HashMap;

class Solution {
    public String[] solution(String[] record) {
        
        int cnt=0;
        HashMap <String, String>iduser=new HashMap<>();
        for(int i=0; i<record.length; i++){
            String[] temp=record[i].split(" ");
            if(temp[0].equals("Enter") || temp[0].equals("Change")){ //Enter, Change이면 유저아이디와 닉네임 추가
                iduser.put(temp[1],temp[2]);
                if(temp[0].equals("Enter")){ //answer length 구하기
                    cnt++;
                }
            }
            if(temp[0].equals("Leave")){ //answer length 구하기
                cnt++;
            }
        }
        String[] answer = new String[cnt];

        int idx=0;
        for(int i=0; i<record.length; i++){
            String[] temp=record[i].split(" ");
            if(temp[0].equals("Enter")){
                answer[idx++]=iduser.get(temp[1])+"님이 들어왔습니다.";
            }
            else if(temp[0].equals("Leave")){
                answer[idx++]=iduser.get(temp[1])+"님이 나갔습니다.";
            }
        }
        return answer;
    }
}