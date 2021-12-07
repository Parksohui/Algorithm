import java.util.HashMap;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        
        HashMap<Integer,Integer> map = new HashMap<>(); //순위
        map.put(6,1);
        map.put(5,2);
        map.put(4,3);
        map.put(3,4);
        map.put(2,5);
        map.put(1,6);
        map.put(0,6);
        
        int correct=0;
        int zero=0;
        for(int i=0; i<6; i++){
            if (lottos[i]==0){ //알아 볼수 없는 번호
                zero+=1;
            }
            else{
                for(int j=0; j<6; j++){
                    if(lottos[i]==win_nums[j]){ //일치하는 번호
                        correct+=1;
                    }
                }
            }
        }
        answer[0]=map.get(correct+zero); //최고 순위
        answer[1]=map.get(correct); //최저 순위
        
        return answer;
    }
}